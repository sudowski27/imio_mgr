"""version 0.1.0"""
import random
import numpy as np
import pandas as pd
from extend_samples.src.concatenate_device_dataframes import concatenate_device_dataframes


def generate_dataframe(rows: int, cols: int, val: float) -> pd.DataFrame:
    """
    Generate DataFrame with shape(cols, rows)

    Parameters
    ----------
    rows: int
    cols: int
    val: float

    Returns
    -------
    pd.DataFrame
    """
    list_for_dataframe = []
    for _ in range(rows):
        array_for_col = np.full(cols, val)
        list_for_dataframe.append(array_for_col)

    return pd.DataFrame(list_for_dataframe)


def conc_dataframes_list(dataframe_list: list) -> pd.DataFrame:
    """
    Concatenate list of DataFrame objects

    Parameters
    ----------
    dataframe_list: list

    Returns
    -------
    pd.DataFrame
    """
    return pd.concat(dataframe_list, ignore_index=True)


def test_0():
    """
    Test 0

    Test concatenate two DataFrame with diffrent cols shape
    """
    df1_rows = 3
    df1_cols = 2
    df1_val = 0
    df1 = generate_dataframe(df1_rows, df1_cols, df1_val)
    df2_rows = 2
    df2_cols = 4
    df2_val = 1
    df2 = generate_dataframe(df2_rows, df2_cols, df2_val)
    df_list = [df1, df2]
    expected_dataframe = conc_dataframes_list(df_list)
    result = concatenate_device_dataframes(df_list)

    assert result.equals(expected_dataframe)


def test_1():
    """
    Test 1

    Test concatenate two DataFrame with the same cols shape
    """
    df1_rows = 3
    df1_cols = 2
    df1_val = 0
    df1 = generate_dataframe(df1_rows, df1_cols, df1_val)
    df2_rows = 6
    df2_cols = 2
    df2_val = 1
    df2 = generate_dataframe(df2_rows, df2_cols, df2_val)
    df_list = [df1, df2]
    expected_dataframe = conc_dataframes_list(df_list)
    result = concatenate_device_dataframes(df_list)

    assert result.equals(expected_dataframe)
