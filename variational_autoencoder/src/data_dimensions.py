"""version 0.1.0"""
import pandas as pd
from .const_values import CSV_SEPERATOR


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
    """
    return pd.read_csv(filename, sep=CSV_SEPERATOR, header=None)
