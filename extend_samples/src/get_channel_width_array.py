"""version 0.1.0"""
import pandas as pd
import numpy as np


def get_channel_width_array(device_data_frame: pd.DataFrame, channel_width: float) -> np.array:
    """
    Get values channel width of device

    Parameters
    ----------
    device_data_frame: pd.DataFrame
    channel_width: float

    Returns
    -------
    np.array
    """
    rows, _ = device_data_frame.shape

    width_array = np.full((rows,), channel_width)

    return width_array
