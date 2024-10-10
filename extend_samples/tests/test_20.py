"""version 0.1.0"""
import random
import pandas as pd
import numpy as np
from extend_samples.src.get_new_created_device_data_frame import get_new_created_device_data_frame
from extend_samples.src.generate_new_device_dataframes import (
    generate_new_device_dataframes,
    GenerateNewDeviceDataframesArguments
)
from extend_samples.src.device_config_keys import device_config_keys


def create_device_config() -> dict:
    """
    Create device configure

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
    data = {}
    data["1"] = device_0_data

    return data


def create_devices_list() -> list:
    """
    Create devices list

    Returns
    -------
    list
    """
    return []


def create_last_device_number() -> int:
    """
    Create device last number

    Returns
    -------
    int
    """
    return 1


def generate_orginal_dataframe() -> pd.DataFrame:
    """
    Generate DataFrame from measures

    Returns
    -------
    pd.DataFrame
    """
    orginal_dataframe_length = 100
    orginal_dataframe_device_number = 1
    uniform_lower_limit = 0.0
    uniform_upper_limit = 1.0
    device_1_data = []
    for _ in range(orginal_dataframe_length):
        single_data = [orginal_dataframe_device_number,
                       random.uniform(uniform_lower_limit, uniform_upper_limit),
                       random.uniform(uniform_lower_limit, uniform_upper_limit),
                       random.uniform(uniform_lower_limit, uniform_upper_limit)
                       ]
        device_1_data.append(single_data)
    device_1_data_frame = pd.DataFrame(device_1_data)
    return device_1_data_frame


def generate_device_coeffs() -> np.array:
    """
    Generate device coeffs

    Returns
    -------
    np.array
    """
    device_coeffs_shape = (9,)
    uniform_lower_limit = 0.0
    uniform_upper_limit = 1.0
    device_coeffs = np.zeros(device_coeffs_shape)
    for i in range(device_coeffs_shape[0]):
        device_coeffs[i] = random.uniform(uniform_lower_limit, uniform_upper_limit)
    return device_coeffs


def generate_channel_width() -> float:
    """
    Generare channel width

    Returns
    -------
    float
    """
    return 130e-6


def generate_reference(device_config: tuple,
                       devices_list: list,
                       orginal_dataframe: pd.DataFrame,
                       last_device_number: int,
                       device_coeffs: np.array,
                       channel_width: float) -> tuple:
    """
    Generate reference for test

    Parameters
    ----------
    device_config: tuple,
    devices_list: list
    orginal_dataframe: pd.DataFrame
    last_device_number: int
    device_coeffs: np.array
    channel_width: float

    Returns
    -------
    tuple
        (devices_list, last_device_number)
    """
    dev_list = devices_list + [orginal_dataframe]
    last_device_number = last_device_number + 1

    case = device_config["1"][device_config_keys.cases][0]
    generated_device = get_new_created_device_data_frame(
        case,
        orginal_dataframe,
        last_device_number,
        device_coeffs,
        channel_width
    )
    dev_list.append(generated_device)
    last_device_number += 1

    return dev_list, last_device_number


def test_0():
    """
    Test 0

    Test generating new device dataframes
    """
    device_config = create_device_config()
    devices_list = create_devices_list()
    orginal_dataframe = generate_orginal_dataframe()
    last_device_number = create_last_device_number()
    device_coeffs = generate_device_coeffs()
    channel_width = generate_channel_width()

    expected_dev_list, expected_last_device_number = generate_reference(
        device_config,
        devices_list,
        orginal_dataframe,
        last_device_number,
        device_coeffs,
        channel_width
    )

    dev_num = 1

    arguments = GenerateNewDeviceDataframesArguments(
        devices_list,
        device_config[str(dev_num)],
        orginal_dataframe,
        last_device_number,
        device_coeffs,
        channel_width
    )
    result_dev_list, result_last_dev_number = generate_new_device_dataframes(
        arguments
    )

    assert all(df1.equals(df2) for df1, df2 in zip(result_dev_list, expected_dev_list))
    assert result_last_dev_number == expected_last_device_number
