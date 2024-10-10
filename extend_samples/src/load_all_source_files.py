"""version 0.1.0"""
import configparser
from .config_file_keys import config_keys


def load_all_source_files(config: configparser.ConfigParser) -> dict:
    """
    Load all source files with samples from config

    Expected config file structure:

    [Source]
    path_0 = path_0_value
    path_1 = path_1_value
    [Destination]
    path_0 = path_0_value
    path_1 = path_1_value

    Parameters
    ----------
    config: configparser.ConfigParser

    Returns
    -------
    dict
    """
    source_files = dict(config[config_keys.source].items())

    return source_files
