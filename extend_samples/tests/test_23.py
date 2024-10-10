"""version 0.1.0"""
import pandas as pd
from extend_samples.src.join_channel_width_to_device_dataframe import join_channel_width_to_device_dataframe


def test_0():
    """
    Test 0

    Test joining new column
    """
    device_1_data = [
        [1, 0.0, 5e-2, 2e-12],
        [1, 0.0, 6e-2, 4e-12]
    ]
    device_1_data_frame = pd.DataFrame(device_1_data)
    channel_width = 0.1

    expected_data = [
        [1, 0.0, 5e-2, 2e-12, channel_width],
        [1, 0.0, 6e-2, 4e-12, channel_width]
    ]
    expected_dataframe = pd.DataFrame(expected_data)

    result = join_channel_width_to_device_dataframe(device_1_data_frame, channel_width)

    assert result.equals(expected_dataframe)
