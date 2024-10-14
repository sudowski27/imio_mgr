"""version 0.1.0"""
import pytest
from variational_autoencoder.src.validate_configuration import validate_device
from .helpers.create_configure_dict import create_configure_dict


def test_0():
    """
    Test 0

    Test if data is valid
    """
    configure_dict = create_configure_dict()
    validate_device(configure_dict)


def test_1():
    """
    Test 1

    Test if value type is bad
    """
    create_configure_dict_kwargs = {
        "device_value": True
    }
    configure_dict = create_configure_dict(**create_configure_dict_kwargs)
    with pytest.raises(ValueError):
        validate_device(configure_dict)


def test_2():
    """
    Test 2

    Test if key is missing
    """
    create_configure_dict_kwargs = {
        "device_key": True
    }
    configure_dict = create_configure_dict(**create_configure_dict_kwargs)
    with pytest.raises(ValueError):
        validate_device(configure_dict)
