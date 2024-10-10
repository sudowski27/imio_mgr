"""version 0.1.0"""
import pandas as pd
from .const_values import DEVICE_INDEX


def get_device_number(device_data_frame: pd.DataFrame) -> int:
    """
    Get Device Number from DataFrame series

    Parameters
    ----------
    device_data_frame: int

    Returns
    -------
    int
    """
    first_row = 0
    device_number = device_data_frame[DEVICE_INDEX].values[first_row]

    return device_number
