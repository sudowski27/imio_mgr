"""version 0.1.0"""
import pandas as pd
from .const_values import DEVICE_INDEX


def split_csv_object_by_device(csv_object: pd.DataFrame) -> list:
    """
    Split DataFrame object into list with DataFrame objects with single device

    DataFrame expected format:
    device_num val_0 val_1 ...

    Parameters
    ----------
    csv_object: pd.DataFrame

    Returns
    -------
    list
    """
    grouped = csv_object.groupby(csv_object[DEVICE_INDEX])

    dataframes = [group.reset_index(drop=True) for _, group in grouped]

    return dataframes
