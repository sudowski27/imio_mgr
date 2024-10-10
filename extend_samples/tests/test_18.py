"""version 0.1.0"""
import random
import numpy as np
import pandas as pd
from extend_samples.src.get_drain_to_source_voltage_array import get_drain_to_source_voltage_array
from extend_samples.src.get_gate_to_source_voltage_array import get_gate_to_source_voltage_array
from extend_samples.src.get_drain_current_array import get_drain_current_array
from extend_samples.src.get_arguments_tuple import get_arguments_tuple
from extend_samples.src.mosfet_function import mosfet_function
from extend_samples.src.get_new_created_device_data_frame import get_new_created_device_data_frame
from extend_samples.src.device_config_keys import device_config_keys


def generate_case() -> dict:
    """
    Generate case for test

    Returns
    -------
    dict
    """
    channel_length_key = "channel_length"
    temperature_key = "temperature"
    channel_length_value = 140e-9
    temperature_value = 450.0

    case = {
        channel_length_key: channel_length_value,
        temperature_key: temperature_value
    }
    return case


def generate_last_device_number() -> int:
    """
    Generare last device number

    Returns
    -------
    int
    """
    return 1


def generate_channel_width() -> float:
    """
    Generare channel width

    Returns
    -------
    float
    """
    return 130e-6


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


def generate_reference_dataframe(case: dict, last_device_number: int,
                                 device_coeffs: np.array,
                                 orginal_dataframe: pd.DataFrame,
                                 channel_width: float) -> pd.DataFrame:
    """
    Generate reference dataframe

    Parameters
    ----------
    case: dict
    last_device_number: int
    device_coeffs: np.array
    orginal_dataframe: pd.DataFrame
    channel_width: float

    Returns
    -------
    pd.DataFrame
    """
    v_ds_array = get_drain_to_source_voltage_array(orginal_dataframe)
    v_gs_array = get_gate_to_source_voltage_array(orginal_dataframe)
    arguments = get_arguments_tuple(orginal_dataframe, channel_width)
    reconstruction_drain_current = np.zeros_like(v_gs_array)

    list_to_create_dataframe = []

    for i in range(len(reconstruction_drain_current)):
        argument = (arguments[0][i], arguments[1][i], arguments[2][i])
        reconstruction_drain_current[i] = mosfet_function(
            argument,
            device_coeffs[0],
            case[device_config_keys.temperature],
            device_coeffs[2],
            device_coeffs[3],
            case[device_config_keys.channel_length],
            device_coeffs[5],
            device_coeffs[6],
            device_coeffs[7],
            device_coeffs[8]
        )
        list_to_create_dataframe.append(
            [last_device_number,
             v_gs_array[i],
             v_ds_array[i],
             reconstruction_drain_current[i],
             channel_width
             ]
        )

    reference_dataframe = pd.DataFrame(list_to_create_dataframe)
    return reference_dataframe


def test_0():
    """
    Test 0

    Test generating new dataframe
    """
    case = generate_case()
    last_device_number = generate_last_device_number()
    device_coeffs = generate_device_coeffs()
    orginal_dataframe = generate_orginal_dataframe()
    channel_width = generate_channel_width()

    reference_dataframe = generate_reference_dataframe(
        case,
        last_device_number,
        device_coeffs,
        orginal_dataframe,
        channel_width
    )

    result = get_new_created_device_data_frame(
        case,
        orginal_dataframe,
        last_device_number,
        device_coeffs,
        channel_width
    )

    assert result.equals(reference_dataframe)
