"""version 0.1.0"""
import pandas as pd
import numpy as np
from .const_values import CHANNEL_WIDTH_INDEX_DATA_FRAME


def join_channel_width_to_device_dataframe(dataframe: pd.DataFrame, channel_width: float) -> pd.DataFrame:
    """
    Join channel width to orginal device dataframe

    Parameters
    ----------
    dataframe: pd.DataFrame
    channel_width: float

    Returns
    -------
    pd.DataFrame
    """
    dataframe_copy = dataframe.copy()
    rows_shape_index = 0
    rows = dataframe_copy.shape[rows_shape_index]
    channel_width_column = np.full(rows, channel_width)
    dataframe_copy[CHANNEL_WIDTH_INDEX_DATA_FRAME] = channel_width_column

    return dataframe_copy
