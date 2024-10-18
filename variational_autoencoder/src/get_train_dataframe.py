"""version 0.1.0"""
import pandas as pd
from .data_dimensions import (
    load_dataframe,
    is_devices_seperated,
    connect_devices
)
from .configuration_keys import configuration_keys


def get_train_dataframe(configuration: dict) -> pd.DataFrame:
    """
    Get train dataframe from csv file

    Parameters
    ----------
    configuration: dict

    Returns
    -------
    pd.DataFrame
    """
    filename = configuration[configuration_keys.train_dataset_file]
    return get_train_dataframe_filename(filename)


def get_train_dataframe_filename(filename: str) -> pd.DataFrame:
    """
    Get train dataframe from csv file

    Parameters
    ----------
    filename: str

    Returns
    -------
    pd.DataFrame
    """
    dataframe = load_dataframe(filename)

    if is_devices_seperated(dataframe):
        dataframe = connect_devices(dataframe)
    return dataframe
