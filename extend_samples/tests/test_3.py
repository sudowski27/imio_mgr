"""version 0.1.0"""
import pytest
from extend_samples.src.get_config_for_device import get_config_for_device


def create_data() -> dict:
    """
    Create data

    Returns
    -------
    dict
    """
    device_0_data = {
        "number_of_cases": 1,
        "cases": [
            {"channel_length": 1, "temperature": 20}
        ]
    }
    device_1_data = {
        "number_of_cases": 1,
        "cases": [
            {"channel_length": 2, "temperature": 30}
        ]
    }
    data = {}
    data["1"] = device_0_data
    data["2"] = device_1_data

    return data


def test_0():
    """
    Test 0

    Test load data for existing device
    """
    data = create_data()
    device_number = 1

    expected_data = data[str(device_number)]
    result = get_config_for_device(data, device_number)
    assert expected_data == result


def test_1():
    """
    Test 1

    Test load data for no existing device
    """
    data = create_data()
    device_number = 3

    with pytest.raises(KeyError):
        get_config_for_device(data, device_number)
