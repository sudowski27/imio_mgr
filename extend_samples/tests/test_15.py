"""version 0.1.0"""
import configparser
from extend_samples.src.config_file_keys import config_keys
from extend_samples.src.get_channel_width_for_csv import get_channel_width_for_csv


def create_ini_config() -> configparser.ConfigParser():
    """
    Create config

    Returns
    -------
    configparser.ConfigParser
    """
    config = configparser.ConfigParser()
    config[config_keys.channel_width] = {
        'path_0': 130e-9
    }

    return config


def test_0():
    """
    Test 0

    Test getting channel width
    """
    config = create_ini_config()
    path = "path_0"
    expected_width = 130e-9
    delta = 1e-6
    channel_width = get_channel_width_for_csv(config, path)

    assert abs(expected_width - channel_width) <= delta
