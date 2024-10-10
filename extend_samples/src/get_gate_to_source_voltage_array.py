"""version 0.1.0"""
import pandas as pd
import numpy as np
from .const_values import GATE_TO_SOURCE_VOLTAGE_INDEX_DATA_FRAME


def get_gate_to_source_voltage_array(device_data_frame: pd.DataFrame) -> np.array:
    """
    Get values of column with v_gs

    Parameters
    ----------
    device_data_frame: pd.DataFrame

    Returns
    -------
    np.array
    """
    gate_to_source_voltage_values = device_data_frame[GATE_TO_SOURCE_VOLTAGE_INDEX_DATA_FRAME]
    gate_to_source_voltage_values_array = gate_to_source_voltage_values.to_numpy()

    return gate_to_source_voltage_values_array
