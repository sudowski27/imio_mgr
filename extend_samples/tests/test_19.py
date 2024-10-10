"""version 0.1.0"""
import pandas as pd
from extend_samples.src.change_dataframe_device_number import change_dataframe_device_number


def test_0():
    """
    Test 0

    Testing change device number in DataFrame
    """
    device_1_data = [
        [1, 0.0, 5e-2, 2e-12],
        [1, 0.0, 6e-2, 4e-12]
    ]
    device_1_data_frame = pd.DataFrame(device_1_data)
    new_device_number = 2

    device_2_data = [
        [new_device_number, 0.0, 5e-2, 2e-12],
        [new_device_number, 0.0, 6e-2, 4e-12]
    ]
    expected_value = pd.DataFrame(device_2_data)

    result = change_dataframe_device_number(device_1_data_frame, new_device_number)

    assert result.equals(expected_value)
