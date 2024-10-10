"""version 0.1.0"""
import configparser
from .config_file_keys import config_keys


def get_csv_filename(config: configparser.ConfigParser, path: str) -> str:
    """
    Get filename of destination csv

    Parameters
    ----------
    config: configparser.ConfigParser
    path: str

    Returns
    -------
    str
    """
    return config[config_keys.destination][path]
