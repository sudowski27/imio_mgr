"""version 0.1.0"""
import pandas as pd
import numpy as np
from .const_values import DEVICE_INDEX


def change_dataframe_device_number(device_dataframe: pd.DataFrame, new_device_number: int) -> pd.DataFrame:
    """
    Change device number in DataFrame

    Parameters
    ----------
    device_dataframe: pd.DataFrame
    new_device_number: int

    Returns
    -------
    pd.DataFrame
    """
    device_dataframe_copy = device_dataframe.copy()
    device_dataframe_shape = device_dataframe.shape
    shape_row_index = 0
    rows = device_dataframe_shape[shape_row_index]
    new_column = np.full((rows,), new_device_number)

    device_dataframe_copy[DEVICE_INDEX] = new_column

    return device_dataframe_copy
