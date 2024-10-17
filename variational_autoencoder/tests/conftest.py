"""version 0.1.0"""

import pytest
import pandas as pd


@pytest.fixture
def one_and_two_devices_dataframe():
    """
    Fikstura, która tworzy przykładowy DataFrame.

    Returns
    -------
    tuple
        (dataframe_one_device, dataframe_two_devices)
    """
    data_1_dataframe = [
        [1, 200, 0.1, 0.1, 0.2],
        [1, 200, 0.2, 0.4, 0.6]
    ]

    data_2_dataframe = [
        [2, 200, 0.1, 0.1, 0.2],
        [2, 200, 0.2, 0.4, 0.6]
    ]

    dataframe_one_device = pd.DataFrame(data_1_dataframe)
    dataframe_two_devices = pd.DataFrame(data_1_dataframe + data_2_dataframe)

    return dataframe_one_device, dataframe_two_devices
