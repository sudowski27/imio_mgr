"""version 0.1.0"""
from variational_autoencoder.src.data_dimensions import (
    validate_dataframe,
    get_first_device
)


def test_0(one_and_two_devices_dataframe):
    """
    Test 0

    Test getting first device

    Parameters
    ----------
    one_and_two_devices_dataframe: fixture
    """
    expected_dataframe, dataframe = one_and_two_devices_dataframe

    validate_dataframe(dataframe)
    dataframe_with_first_device = get_first_device(dataframe)

    assert dataframe_with_first_device.equals(expected_dataframe)
