#!/usr/bin/python3.6

# ======================================================================================================================
# VCenter API Client
# Author: Robin LIORET
# API Documentation : https://developer.vmware.com/apis/vsphere-automation/v7.0.0/vcenter/
# ======================================================================================================================
from __future__ import annotations
import json
import logging
from dataclasses import dataclass
from typing import Optional, Union

import requests
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning

from smr import get_dummy_logger, load_yaml

VALID_RETURN_CODES = {200, 201}


def disable_warnings():
    """Disable the warning of the requests package."""
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


class VCenterConnectionError(Exception):
    """Exception raised when the connection to the vcenter failed."""


@dataclass
class VCenterAPIClient(object):
    """API client for a VMWare VCenter."""
    _url: str
    _api_timeout: int
    _api_session: requests.Session
    _auth: HTTPBasicAuth
    _logger: logging.Logger

    def connect(self) -> VCenterAPIClient:
        """Create the connection with the vCenter."""
        self._logger.debug(f'Connecting to {self._url}...')
        self._api_session.post(self._build_url('/rest/com/vmware/cis/session'), auth=self._auth)
        self._logger.info(f'Connected to {self._url}')
        return self

    def close(self) -> VCenterAPIClient:
        """Close the connection with the vCenter."""
        self._api_session.close()
        self._logger.info(f'Connection to {self._url} closed')
        return self

    def query(self,
              path: str,
              method: str = 'get',
              data: Optional[Union[dict, list]] = None,
              params: Optional[Union[dict]] = None,
              max_tries: int = 5) -> Optional[Union[dict, list]]:
        """Perform a query on the API. Will try *max_tries* time before throwing an error."""
        url = self._build_url(path)
        self._logger.debug(f'API request "{method}" on {url}')
        for i in range(max_tries):
            try:
                return self._query(path, method, data, params)
            except VCenterConnectionError as ex:
                self._logger.error(f'Request "{method}" failed on {url} (Try {i + 1}/{max_tries})\n\t{ex}')
                self.connect()
        else:
            raise VCenterConnectionError(f'Request "{method}" on {url} failed {max_tries} times')

    def get(self, path: str, params: Optional[dict] = None) -> Optional[Union[dict, list]]:
        return self.query(path=path, method='get', params=params)

    def post(self, path: str, data: Union[dict, list], params: Optional[dict] = None) -> Optional[Union[dict, list]]:
        return self.query(path=path, method='post', data=data, params=params)

    def patch(self, path: str, data: Union[dict, list], params: Optional[dict] = None) -> Optional[Union[dict, list]]:
        return self.query(path=path, method='patch', data=data, params=params)

    def delete(self, path: str, params: Optional[dict] = None) -> Optional[Union[dict, list]]:
        return self.query(path=path, method='delete', params=params)

    def _query(self, path, method, data, params) -> Optional[Union[dict, list]]:
        params = params or {}
        if data is not None:
            data = json.dumps(data)
        resp = self._api_session.__getattribute__(method)(
            self._build_url(path),
            params=params,
            data=data,
            timeout=self._api_timeout,
            auth=self._auth
        )
        result = resp.json()
        if resp.status_code not in VALID_RETURN_CODES:
            raise VCenterConnectionError(resp.text)
        return result.get('value', None)

    def _build_url(self, path=''):
        return "{}{}".format(self._url, path)


def create_vcenter_api_client(
        url: str,
        username: str,
        password: str,
        timeout: Optional[int] = None,
        ssl_verify: Optional[bool] = True,
        logger: Optional[logging.Logger] = None) -> VCenterAPIClient:
    """Create a vCenter API client."""
    session = requests.Session()
    session.verify = ssl_verify
    auth = HTTPBasicAuth(username, password)
    logger = logger or get_dummy_logger()

    return VCenterAPIClient(
        url,
        timeout,
        session,
        auth,
        logger
    )


def create_vcenter_api_client_from_dict(config: dict) -> VCenterAPIClient:
    """Create a vcenter api client from the given dictionary."""
    return create_vcenter_api_client(**config)


def create_vcenter_api_client_from_yaml(filename: str) -> VCenterAPIClient:
    """Create a vcenter api client from the given yaml configuration file."""
    config = load_yaml(filename)
    return create_vcenter_api_client_from_dict(config)


def create_bulk_vcenter_api_clients(configs: list[dict]) -> list[VCenterAPIClient]:
    """Create a bunch of VCenter API clients from the given configurations."""
    return [create_vcenter_api_client_from_dict(config) for config in configs]


def create_bulk_vcenter_api_clients_from_yaml(filename: str) -> list[VCenterAPIClient]:
    """Create a bunch of VCenter API clients from the given yaml configuration file."""
    return create_bulk_vcenter_api_clients(load_yaml(filename))
