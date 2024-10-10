"""version 0.1.0"""
import configparser
from extend_samples.src.config_file_keys import config_keys
from extend_samples.src.get_csv_filename import get_csv_filename


def create_ini_config() -> configparser.ConfigParser():
    """
    Create config

    Returns
    -------
    configparser.ConfigParser
    """
    config = configparser.ConfigParser()
    config[config_keys.destination] = {
        'path_0': 'path_to_csv'
    }

    return config


def test_0():
    """
    Test 0

    Test load csv destination filename
    """
    path = "path_0"
    config = create_ini_config()
    expected_value = "path_to_csv"

    result = get_csv_filename(config, path)
    assert result == expected_value
