"""version 0.1.0"""
import pandas as pd
from .const_values import CSV_SEPERATOR


def load_csv_file(file_name: str) -> pd.DataFrame:
    """
    Load csv file

    Paremeters
    ----------
    file_name: str

    Returns
    -------
    pd.DataFrame
    """
    data = pd.read_csv(file_name, sep=CSV_SEPERATOR, header=None)
    return data
