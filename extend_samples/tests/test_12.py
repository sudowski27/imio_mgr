"""version 0.1.0"""
import pandas as pd
import numpy as np
from extend_samples.src.get_arguments_tuple import get_arguments_tuple


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
    array_0 = np.array([0.0, 0.0])
    array_1 = np.array([5e-2, 6e-2])
    array_2 = np.full(shape=(len(device_1_data),), fill_value=channel_width)

    expected_value = (array_0, array_1, array_2)

    result = get_arguments_tuple(device_1_data_frame, channel_width)
    comparison_results = [np.array_equal(a, b) for a, b in zip(expected_value, result)]

    assert all(comparison_results)
