"""version 0.1.0"""
import pandas as pd
from .get_gate_to_source_voltage_array import get_gate_to_source_voltage_array
from .get_drain_to_source_voltage_array import get_drain_to_source_voltage_array
from .get_channel_width_array import get_channel_width_array


def get_arguments_tuple(device_data_frame: pd.DataFrame, channel_width: float) -> tuple:
    """
    Get values of arguments to find coeffs

    Parameters
    ----------
    device_data_frame: pd.DataFrame
    channel_width: float

    Returns
    -------
    tuple
        (v_gs_array, v_ds_array, channel_width_array)
    """
    v_gs_array = get_gate_to_source_voltage_array(device_data_frame)
    v_ds_array = get_drain_to_source_voltage_array(device_data_frame)
    channel_width_array = get_channel_width_array(device_data_frame, channel_width)

    return (v_gs_array, v_ds_array, channel_width_array)
