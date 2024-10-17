"""version 0.1.3"""
import pandas as pd
from .const_values import (
    CSV_SEPERATOR,
    DATAFRAME_EXPECTED_COLUMNS,
    DEVICE_INDEX,
    DEVICE_DTYPE,
    CHANNEL_WIDTH_INDEX,
    CHANNEL_WIDTH_DTYPE,
    VOLTAGE_CURRENT_D_TYPE,
    DEVICE_MINIMUM_VALUE
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
    device_count_in_column = (dataframe[DEVICE_INDEX] == DEVICE_MINIMUM_VALUE).sum()

    device_index = dataframe[DEVICE_INDEX].eq(DEVICE_MINIMUM_VALUE).idxmax()

    device_count_in_row = 0
    for value in dataframe[DEVICE_INDEX][device_index:]:
        if value == DEVICE_MINIMUM_VALUE:
            device_count_in_row += 1
        else:
            break

    return device_count_in_column != device_count_in_row


def connect_devices(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Create dataframe with connected devices

    Parameters
    ----------
    dataframe: pd.DataFrame

    Returns
    -------
    pd.DataFrame
    """
    dataframe_copy = dataframe.copy()
    dataframe_copy['original_index'] = dataframe_copy.index

    dataframe_copy = dataframe_copy.sort_values(by=[DEVICE_INDEX, 'original_index'], ignore_index=True)
    dataframe_copy.drop(columns=['original_index'], inplace=True)

    return dataframe_copy
