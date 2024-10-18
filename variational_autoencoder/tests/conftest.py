"""version 0.1.2"""

import pytest
import pandas as pd
from variational_autoencoder.src.const_values import (
    CPU_DEVICE,
    CUDA_DEVICE
)
from variational_autoencoder.src.configuration_keys import configuration_keys


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


@pytest.fixture
def small_configure_with_device_cpu():
    """
    Fixture with configure dict with cpu device

    Returns
    -------
    dict
    """
    configure = {
        configuration_keys.device: CPU_DEVICE
    }
    return configure


@pytest.fixture
def small_configure_with_device_cuda():
    """
    Fixture with configure dict with cuda device

    Returns
    -------
    dict
    """
    configure = {
        configuration_keys.device: CUDA_DEVICE
    }
    return configure


@pytest.fixture
def small_configure_with_train_dataset_file():
    """
    Fixture with configure dict with cuda device

    Returns
    -------
    dict
    """
    configure = {
        configuration_keys.train_dataset_file: "test_csv.csv"
    }
    return configure
