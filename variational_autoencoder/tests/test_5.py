"""version 0.1.0"""
import pytest
from variational_autoencoder.src.validate_configuration import validate_synth_data_file_name_core
from .helpers.create_configure_dict import create_configure_dict


def test_0():
    """
    Test 0

    Test if data is valid
    """
    configure_dict = create_configure_dict()
    validate_synth_data_file_name_core(configure_dict)


def test_1():
    """
    Test 1

    Test if value type is bad
    """
    create_configure_dict_kwargs = {
        "synth_data_file_name_core_value": True
    }
    configure_dict = create_configure_dict(**create_configure_dict_kwargs)
    with pytest.raises(ValueError):
        validate_synth_data_file_name_core(configure_dict)


def test_2():
    """
    Test 2

    Test if key is missing
    """
    create_configure_dict_kwargs = {
        "synth_data_file_name_core_key": True
    }
    configure_dict = create_configure_dict(**create_configure_dict_kwargs)
    with pytest.raises(ValueError):
        validate_synth_data_file_name_core(configure_dict)
