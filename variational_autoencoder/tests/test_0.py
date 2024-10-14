"""version 0.1.1"""
import pytest
from variational_autoencoder.src.load_configuration import load_configuration
from .helpers.create_json_configure_file import create_json_configure_file
from .helpers.remove_file import remove_file


def test_0():
    """
    Test 0

    Test loading good JSON file
    """
    configure_filename = "config.json"
    expected_config = create_json_configure_file(configure_filename)

    test_result = load_configuration(
        configure_filename
    )
    assert test_result == expected_config
    remove_file(configure_filename)


def test_1():
    """
    Test 1

    Test loading bad JSON file
    """
    configure_filename = "config.json"
    create_json_configure_file(
        configure_filename,
        is_json_syntax_good=False
    )

    with pytest.raises(ValueError):
        load_configuration(
            configure_filename
        )
    remove_file(configure_filename)
