"""version 0.1.0"""
import pandas as pd
import numpy as np
from .const_values import DRAIN_TO_SOURCE_VOLTAGE_INDEX_DATA_FRAME


def get_drain_to_source_voltage_array(device_data_frame: pd.DataFrame) -> np.array:
    """
    Get values of column with v_ds

    Parameters
    ----------
    device_data_frame: pd.DataFrame

    Returns
    -------
    np.array
    """
    drain_to_source_voltage_values = device_data_frame[DRAIN_TO_SOURCE_VOLTAGE_INDEX_DATA_FRAME]
    drain_to_source_voltage_values_array = drain_to_source_voltage_values.to_numpy()

    return drain_to_source_voltage_values_array
