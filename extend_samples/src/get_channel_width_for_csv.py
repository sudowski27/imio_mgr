"""version 0.1.0"""
import configparser
from .config_file_keys import config_keys


def get_channel_width_for_csv(config: configparser.ConfigParser, path: str) -> float:
    """
    Get channel width for devices in one csv file

    Parameters
    ----------
    config: configparser.ConfigParser
    path: str

    Returns
    -------
    float
    """
    return float(config[config_keys.channel_width][path])
