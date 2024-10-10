"""version 0.1.0"""
import copy
from dataclasses import dataclass
import pandas as pd
import numpy as np
from .device_config_keys import device_config_keys
from .change_dataframe_device_number import change_dataframe_device_number
from .get_new_created_device_data_frame import get_new_created_device_data_frame


@dataclass
class GenerateNewDeviceDataframesArguments:
    """
    Class with arguments for function
    generate_new_device_dataframes

    Parameters
    ----------
    devices_list: list
    device_config: dict
    orginal_dataframe: pd.DataFrame
    last_device_number: int
    device_coeffs: np.array
    channel_width: float
    """
    devices_list: list
    device_config: dict
    orginal_dataframe: pd.DataFrame
    last_device_number: int
    device_coeffs: np.array
    channel_width: float


def generate_new_device_dataframes(arguments: GenerateNewDeviceDataframesArguments) -> tuple:
    """
    Generate new device dataframes: orginal dataframe, and new generated

    Parameters
    ----------
    arguments: GenerateNewDeviceDataframesArguments

    Returns
    -------
    tuple
        (devices_list, last_device_number)
    """
    number_of_cases = arguments.device_config[device_config_keys.number_of_cases]
    devices_list_copy = copy.deepcopy(arguments.devices_list)

    edited_orginal_dataframe = change_dataframe_device_number(
        arguments.orginal_dataframe,
        arguments.last_device_number
    )
    devices_list_copy.append(edited_orginal_dataframe)

    last_device_number = arguments.last_device_number + 1

    for i in range(number_of_cases):
        case = arguments.device_config[device_config_keys.cases][i]

        new_device_dataframe = get_new_created_device_data_frame(
            case,
            edited_orginal_dataframe,
            last_device_number,
            arguments.device_coeffs,
            arguments.channel_width
        )
        devices_list_copy.append(new_device_dataframe)
        last_device_number = last_device_number + 1

    return devices_list_copy, last_device_number
