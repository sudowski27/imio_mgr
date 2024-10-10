"""version 0.1.0"""
import pandas as pd
from .const_values import CSV_SEPERATOR


def save_dataframe_to_csv(dataframe: pd.DataFrame, filename: str) -> None:
    """
    Save dataframe to csv

    Parameters
    ----------
    dataframe: pd.DataFrame
    filename: str
    """
    dataframe.to_csv(filename, sep=CSV_SEPERATOR, index=False)
