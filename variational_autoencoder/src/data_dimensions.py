"""version 0.1.1"""
import pandas as pd
from .const_values import (
    CSV_SEPERATOR,
    DATAFRAME_EXPECTED_COLUMNS,
    DEVICE_INDEX,
    DEVICE_DTYPE,
    CHANNEL_WIDTH_INDEX,
    CHANNEL_WIDTH_DTYPE,
    VOLTAGE_CURRENT_D_TYPE
)


def load_dataframe(filename: str) -> pd.DataFrame:
    """
    Load data from csv to pandas DataFrame

    Parameters
    ----------
    filename: str

    Returns
    -------
    pd.DataFrame

    Raises
    ------
    FileNotFoundError
    ValueEroor
        File with no content
    """
    try:
        return pd.read_csv(filename, sep=CSV_SEPERATOR, header=None)
    except pd.errors.EmptyDataError as exc:
        raise ValueError(f"Empty {filename} file") from exc


def validate_dataframe(dataframe: pd.DataFrame) -> None:
    """
    Validate datafrme: check dimensions and datatypes

    Parameters
    ----------
    dataframe: pd.Dataframe

    Raises
    ------
    ValueError
    """
    _, columns = dataframe.shape
    if columns != DATAFRAME_EXPECTED_COLUMNS:
        raise ValueError(f"csv file have {columns} columns, but {DATAFRAME_EXPECTED_COLUMNS} expected")

    if not dataframe[DEVICE_INDEX].dtype == DEVICE_DTYPE:
        raise ValueError(f"csv file in column {DEVICE_INDEX} have type {dataframe[DEVICE_INDEX].dtype}"
                         f" but expected {DEVICE_DTYPE}")

    if not dataframe[CHANNEL_WIDTH_INDEX].dtype == CHANNEL_WIDTH_DTYPE:
        raise ValueError(f"csv file in column {CHANNEL_WIDTH_INDEX} have type {dataframe[CHANNEL_WIDTH_INDEX].dtype}"
                         f" but expected {CHANNEL_WIDTH_DTYPE}")

    for index in range(2, DATAFRAME_EXPECTED_COLUMNS):
        if not dataframe[index].dtype == VOLTAGE_CURRENT_D_TYPE:
            raise ValueError(f"csv file in column {index} have type {dataframe[index].dtype}"
                             f" but expected {VOLTAGE_CURRENT_D_TYPE}")


def is_devices_seperated(dataframe: pd.DataFrame) -> bool:
    """
    Check is device in dataframe from csv file are seperated

    Parameters
    ----------
    dataframe: pd.DataFrame

    Returns
    -------
    bool
    """
