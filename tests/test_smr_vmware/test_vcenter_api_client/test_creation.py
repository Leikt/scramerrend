import unittest

from smr_vmware.vcenter_api_client import create_vcenter_api_client, VCenterAPIClient, \
    create_vcenter_api_client_from_dict, create_vcenter_api_client_from_yaml, create_bulk_vcenter_api_clients, \
    create_bulk_vcenter_api_clients_from_yaml


class TestVCenterAPIClientCreation(unittest.TestCase):
    def test_create_single_client(self):
        client: VCenterAPIClient = create_vcenter_api_client('test/url', 'dummy', '***secret***')
        self.assertEqual('test/url', client._url)

    def test_create_single_client_from_dict(self):
        config = {
            "url": "test/url",
            "username": "dummy",
            "password": "**secret**"
        }
        client: VCenterAPIClient = create_vcenter_api_client_from_dict(config)
        self.assertEqual('test/url', client._url)

    def test_create_single_client_from_file(self):
        filename = 'test_smr_vmware/test_vcenter_api_client/data/config001.yml'
        client: VCenterAPIClient = create_vcenter_api_client_from_yaml(filename)
        self.assertEqual('test/url', client._url)

    def test_create_bulk_clients(self):
        configs = [
            {
                "url": "test/url",
                "username": "dummy",
                "password": "**secret**"
            },
            {
                "url": "test2/url",
                "username": "dummy2",
                "password": "**secret2**"
            }
        ]
        clients: list[VCenterAPIClient] = create_bulk_vcenter_api_clients(configs)
        self.assertEqual('test/url', clients[0]._url)
        self.assertEqual('test2/url', clients[1]._url)

    def test_create_bulk_clients_from_file(self):
        filename = 'test_smr_vmware/test_vcenter_api_client/data/config002.yml'
        clients: list[VCenterAPIClient] = create_bulk_vcenter_api_clients_from_yaml(filename)
        self.assertEqual('test/url', clients[0]._url)
        self.assertEqual('test2/url', clients[1]._url)