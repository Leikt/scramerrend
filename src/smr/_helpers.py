"""Contain different helper functions."""
import json
import pathlib
from os import PathLike
from typing import Union
import yaml


class UnknownExtensionError(Exception):
    """Exception raised when a file has an unknown extension."""


def load_yaml(path: Union[str, PathLike]) -> Union[dict, list]:
    """Load the content of a yaml file into a dict or a list."""
    path = pathlib.Path(path)
    if not path.name.endswith('.yml'):
        raise UnknownExtensionError(f'Unknown extension .{path.name.split(".")[-1]}')
    return yaml.safe_load(path.read_text())


def save_yaml(path: Union[str, PathLike], data: Union[dict, list]) -> bool:
    """Save the data into a yaml file."""
    path = pathlib.Path(path)
    if not path.name.endswith('.yml'):
        raise UnknownExtensionError(f'Unknown extension .{path.name.split(".")[-1]}')
    path.write_text(yaml.safe_dump(data))
    return True


def load_json(path: Union[str, PathLike]) -> Union[dict, list]:
    """Load the content of a json file into a dict or a list."""
    path = pathlib.Path(path)
    if not path.name.endswith('.json'):
        raise UnknownExtensionError(f'Unknown extension .{path.name.split(".")[-1]}')
    return json.loads(path.read_text())


def save_json(path: Union[str, PathLike], data: Union[dict, list]) -> bool:
    """Save the data into a json file."""
    path = pathlib.Path(path)
    if not path.name.endswith('.json'):
        raise UnknownExtensionError(f'Unknown extension .{path.name.split(".")[-1]}')
    path.write_text(json.dumps(data))
    return True
