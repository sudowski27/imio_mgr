"""version 0.1.0"""
import pandas as pd


def create_empty_csv_file(filename: str) -> None:
    """
    Create empty csv file

    Parameters
    ----------
    filename: str
    """
    dataframe = pd.DataFrame()
    dataframe.to_csv(filename, index=False)
