"""version 0.1.0"""
from dataclasses import dataclass
import numpy as np
import pandas as pd


@dataclass
class CreateCsvColumnsDtypesArgs:
    """
    Parameters
    ----------
    filename: str
    columns: int
    row: int
    types: dict
        {0: "float64"}
    """
    filename: str
    columns: int
    row: int
    types: dict


def create_csv_columns_dtypes(args: CreateCsvColumnsDtypesArgs) -> None:
    """
    Create xml file with pattern

    Parameters
    ----------
    args: CreateXmlColumnsDtypesArgs
    """
    data = {}

    for col in range(args.columns):
        if col in args.types:
            dtype = args.types[col]
            if dtype == "float64":
                data[f"Column_{col}"] = np.random.randn(args.row).astype(np.float64)
            elif dtype == "int":
                data[f"Column_{col}"] = np.random.randint(0, 100, size=args.row).astype(np.int64)
            elif dtype == "str":
                data[f"Column_{col}"] = np.random.choice(['A', 'B', 'C'], size=args.row).astype(str)
        else:
            data[f"Column_{col}"] = np.random.randn(args.row).astype(np.float64)

    df = pd.DataFrame(data)

    df.to_csv(args.filename, index=False, header=None, sep=" ")
