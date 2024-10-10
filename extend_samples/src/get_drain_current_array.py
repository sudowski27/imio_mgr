"""version 0.1.0"""
import pandas as pd
import numpy as np
from .const_values import DRAIN_CURRENT_INDEX_DATA_FRAME


def get_drain_current_array(device_data_frame: pd.DataFrame) -> np.array:
    """
    Get values of column with v_ds

    Parameters
    ----------
    device_data_frame: pd.DataFrame

    Returns
    -------
    np.array
    """
    drain_current_values = device_data_frame[DRAIN_CURRENT_INDEX_DATA_FRAME]
    drain_current_values_array = drain_current_values.to_numpy()

    return drain_current_values_array
