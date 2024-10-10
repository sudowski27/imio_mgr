"""version 0.1.0"""
from dataclasses import dataclass
import pandas as pd
import numpy as np
from .get_drain_to_source_voltage_array import get_drain_to_source_voltage_array
from .get_gate_to_source_voltage_array import get_gate_to_source_voltage_array
from .get_arguments_tuple import get_arguments_tuple
from .get_plot_for_pdf import Coefficients
from .get_plot_for_pdf import HelperCoefficients
from .const_values import coeffs_indexes
from .device_config_keys import device_config_keys
from .mosfet_function import mosfet_function


@dataclass
class Arrays:
    """
    Class storage arrays used in function
    get_new_created_device_data_frame

    Paremeters
    ----------
    v_ds_array: np.array
    v_gs_array: np.array
    drain_current_array: np.array
    """
    v_ds_array: np.array
    v_gs_array: np.array
    drain_current_array: np.array


def get_new_created_device_data_frame(case: dict, orginal_dataframe: pd.DataFrame, last_device_number: int,
                                      device_coeffs: np.array, channel_width: float) -> pd.DataFrame:
    """
    Get dataframe with generated with diffrent coeffs from case

    Paremeters
    ----------
    case: dict
    orginal_dataframe: pd.DataFrame
    last_device_number: int
    device_coeffs: np.array
    channel_width: float

    Returns
    -------
    pd.DataFrame
    """
    arguments = get_arguments_tuple(orginal_dataframe, channel_width)
    arrays = Arrays(
        get_drain_to_source_voltage_array(orginal_dataframe),
        get_gate_to_source_voltage_array(orginal_dataframe),
        None
    )
    arrays.drain_current_array = np.zeros_like(arrays.v_ds_array)

    new_device_dataframe_list = []

    coefficients = Coefficients(
        device_coeffs[coeffs_indexes["mu_0"]],
        case[device_config_keys.temperature],
        device_coeffs[coeffs_indexes["alpha"]],
        device_coeffs[coeffs_indexes["c_ox"]],
        case[device_config_keys.channel_length],
        device_coeffs[coeffs_indexes["lambda_coeff"]],
        device_coeffs[coeffs_indexes["v_th"]]
    )
    helper_coefficients = HelperCoefficients(
        device_coeffs[coeffs_indexes["a"]],
        device_coeffs[coeffs_indexes["b"]]
    )
    array_shape = arguments[0].shape[0]

    for i in range(array_shape):
        argument = (arguments[0][i], arguments[1][i], arguments[2][i])
        arrays.drain_current_array[i] = mosfet_function(argument, coefficients.mu_0, coefficients.t, coefficients.alpha,
                                                 coefficients.c_ox, coefficients.l, coefficients.lambda_coeff,
                                                 coefficients.v_th, helper_coefficients.a, helper_coefficients.b)

        record_list = [last_device_number, arrays.v_gs_array[i], arrays.v_ds_array[i],
                       arrays.drain_current_array[i], channel_width]
        new_device_dataframe_list.append(record_list)

    new_device_dataframe = pd.DataFrame(new_device_dataframe_list)

    return new_device_dataframe
