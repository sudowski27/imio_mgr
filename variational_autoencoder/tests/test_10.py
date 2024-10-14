"""version 0.1.0"""
from variational_autoencoder.src.validate_configuration import validate_configuration
from .helpers.create_configure_dict import create_configure_dict


def test_0():
    """
    Test 0

    Test if data is valid
    """
    configure_dict = create_configure_dict()
    validate_configuration(configure_dict)
