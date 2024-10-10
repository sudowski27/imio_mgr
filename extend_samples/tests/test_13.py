"""version 0.1.0"""
import pandas as pd
import numpy as np
from extend_samples.src.get_drain_current_array import get_drain_current_array


def test_0():
    """
    Test 0

    Test getting numpy array from pandas DataFrame
    """
    device_1_data = [
        [1, 0.0, 5e-2, 2e-12],
        [1, 0.0, 6e-2, 4e-12]
    ]
    device_1_data_frame = pd.DataFrame(device_1_data)
    channel_width = 20
    expected_value = np.array([2e-12, 4e-12])

    result = get_drain_current_array(device_1_data_frame)

    assert np.array_equal(result, expected_value)
