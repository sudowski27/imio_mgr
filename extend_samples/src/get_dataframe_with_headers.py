"""version 0.1.0"""
import pandas as pd
from .dataframe_headers import dataframe_headers
from .const_values import (
    DEVICE_INDEX,
    GATE_TO_SOURCE_VOLTAGE_INDEX_DATA_FRAME,
    DRAIN_TO_SOURCE_VOLTAGE_INDEX_DATA_FRAME,
    DRAIN_CURRENT_INDEX_DATA_FRAME,
    CHANNEL_WIDTH_INDEX_DATA_FRAME
)


def get_dataframe_with_headers(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Get DataFrame with added headers

    headers:
    device v_gs v_ds i_d channel_width

    Parameters
    ----------
    dataframe: pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """
    dataframe_copy = dataframe.copy()
    headers_list_shape = CHANNEL_WIDTH_INDEX_DATA_FRAME + 1
    headers_list_init_val = ""
    headers_list = [headers_list_init_val] * headers_list_shape
    headers_list[DEVICE_INDEX] = dataframe_headers.device
    headers_list[GATE_TO_SOURCE_VOLTAGE_INDEX_DATA_FRAME] = dataframe_headers.v_gs
    headers_list[DRAIN_TO_SOURCE_VOLTAGE_INDEX_DATA_FRAME] = dataframe_headers.v_ds
    headers_list[DRAIN_CURRENT_INDEX_DATA_FRAME] = dataframe_headers.i_d
    headers_list[CHANNEL_WIDTH_INDEX_DATA_FRAME] = dataframe_headers.channel_width

    dataframe_copy.columns = headers_list

    return dataframe_copy
