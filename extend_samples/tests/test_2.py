"""version 0.1.0"""
import configparser
import json
import os
import random
import string
import pytest
from extend_samples.src.config_file_keys import config_keys
from extend_samples.src.get_config_for_csv import get_config_for_csv


def create_ini_config() -> configparser.ConfigParser():
    """
    Create config

    Returns
    -------
    configparser.ConfigParser
    """
    config = configparser.ConfigParser()
    config[config_keys.source] = {
        'path_0': 'path_to_csv'
    }
    config[config_keys.configuration] = {
        'path_0': 'json_0.json'
    }

    return config


def create_good_json_file(config: configparser.ConfigParser) -> dict:
    """
    Create good json file by config

    Parameters
    ----------
    config: configparser.ConfigParser

    Returns
    -------
    dict
    """
    sample_dict = {"1": "A"}
    json_file_name = config[config_keys.configuration]["path_0"]
    json_file_pointer = open(json_file_name, mode="w", encoding="utf-8")
    json.dump(sample_dict, json_file_pointer, indent=4)
    json_file_pointer.close()

    return sample_dict


def create_bad_json_file(config: configparser.ConfigParser) -> None:
    """
    Create good json file by config

    Parameters
    ----------
    config: configparser.ConfigParser
    """
    json_file_name = config[config_keys.configuration]["path_0"]
    json_file_pointer = open(json_file_name, mode="w", encoding="utf-8")
    length = 1000
    letters = string.ascii_letters
    random_string = "".join(random.choice(letters) for _ in range(length))
    json_file_pointer.write(random_string)
    json_file_pointer.close()


def delete_json_file(config: configparser.ConfigParser) -> None:
    """
    Delete json file by config

    Parameters
    ----------
    config: configparser.ConfigParser
    """
    json_file_name = config[config_keys.configuration]["path_0"]
    os.remove(json_file_name)


def test_0():
    """
    Test 0

    Test getting good json_path
    """
    expected_json_path = 'json_0.json'
    config = create_ini_config()
    expected_value = create_good_json_file(config)
    path = "path_0"

    result = get_config_for_csv(config, path)

    assert result == expected_value
    delete_json_file(config)


def test_1():
    """
    Test 1

    Test getting bad json_path
    """
    expected_json_path = 'json_0.json'
    config = create_ini_config()
    path = "path_0"

    with pytest.raises(FileNotFoundError):
        get_config_for_csv(config, path)


def test_2():
    """
    Test 2

    Test getting good json_path with bad json syntax
    """
    expected_json_path = 'json_0.json'
    config = create_ini_config()
    create_bad_json_file(config)
    path = "path_0"

    with pytest.raises(ValueError):
        get_config_for_csv(config, path)

    delete_json_file(config)
