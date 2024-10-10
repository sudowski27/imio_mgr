"""version 0.1.0"""
import configparser
import json
from .config_file_keys import config_keys


def get_config_for_csv(config: configparser.ConfigParser, path: str) -> dict:
    """
    Get config from json file for current path

    Parameters
    ----------
    config: configparser.ConfigParser
    path: str

    Returns
    -------
    dict

    Raises
    ------
    FileNotFoundError
        If json file not found
    ValueError
        If json file have bad syntax
    """
    json_path = config[config_keys.configuration][path]
    with open(json_path, encoding="utf-8") as json_file_pointer:
        try:
            json_dict = json.load(json_file_pointer)
        except json.JSONDecodeError as exc:
            raise ValueError(f"file {path} with syntax error") from exc

    return json_dict
