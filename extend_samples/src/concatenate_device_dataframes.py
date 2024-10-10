"""version 0.1.0"""
import pandas as pd


def concatenate_device_dataframes(devices_list: list) -> pd.DataFrame:
    """
    Returns concatenate DataFrame from list of DataFrames

    Parameters
    ----------
    devices_list: list

    Returns
    -------
    pd.DataFrame
    """
    return pd.concat(devices_list, ignore_index=True)
