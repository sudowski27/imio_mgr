"""version 0.1.0"""
import pandas as pd
from extend_samples.src.get_device_number import get_device_number


def test_0():
    """
    Test 0

    Test get correct device number
    """
    device_1_data = [
        [1, 0.0, 5e-2, 2e-12],
        [1, 0.0, 6e-2, 4e-12]
    ]
    device_1_data_frame = pd.DataFrame(device_1_data)

    expected_device_number = 1

    result = get_device_number(device_1_data_frame)

    assert result == expected_device_number
