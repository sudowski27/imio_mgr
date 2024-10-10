"""version 0.1.0"""
import pandas as pd
from extend_samples.src.dataframe_headers import dataframe_headers
from extend_samples.src.get_dataframe_with_headers import get_dataframe_with_headers


def test_0():
    """
    Test 0

    Test adding headers to dataframe
    """
    device_1_data = [
        [1, 0.0, 5e-2, 2e-12, 0.1],
        [1, 0.0, 6e-2, 4e-12, 0.1]
    ]
    device_1_dataframe = pd.DataFrame(device_1_data)

    columns = [dataframe_headers.device,
               dataframe_headers.v_gs,
               dataframe_headers.v_ds,
               dataframe_headers.i_d,
               dataframe_headers.channel_width]
    expected_value = pd.DataFrame(device_1_data, columns=columns)
    result = get_dataframe_with_headers(device_1_dataframe)

    assert result.equals(expected_value)
