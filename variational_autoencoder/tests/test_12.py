"""version 0.1.0"""
import pytest
from variational_autoencoder.src.data_dimensions import (
    load_dataframe,
    validate_dataframe
)
from .helpers.create_csv_train_dataset_file import create_csv_train_dataset_file, CreateCsvTrainDatasetFileArguments
from .helpers.remove_file import remove_file
from .helpers.create_csv_columns_dtypes import (
    create_csv_columns_dtypes,
    CreateCsvColumnsDtypesArgs
)


def test_0():
    """
    Test 0

    Test detect valid csv file
    """
    filename = "text_csv.csv"
    args = CreateCsvTrainDatasetFileArguments(
        "text_csv.csv",
        5,
        2,
        5,
        5,
        True
    )
    create_csv_train_dataset_file(args)
    dataframe = load_dataframe(filename)
    validate_dataframe(dataframe)
    remove_file(filename)


def test_1():
    """
    Test 1

    Test detect invalid csv: wrong number of columns
    """
    filename = "text_csv.csv"
    args = CreateCsvColumnsDtypesArgs(
        filename,
        3,
        40,
        {
            0: "int",
            1: "int",
            2: "float"
        }
    )
    create_csv_columns_dtypes(args)
    dataframe = load_dataframe(filename)
    with pytest.raises(ValueError):
        validate_dataframe(dataframe)
    remove_file(filename)


def test_2():
    """
    Test 2

    Test detect invalid csv: wrong type 0 column
    """
    filename = "text_csv.csv"
    args = CreateCsvColumnsDtypesArgs(
        filename,
        5,
        40,
        {
            0: "float64",
            1: "int",
            2: "float64",
            3: "float64",
            4: "float64"
        }
    )
    create_csv_columns_dtypes(args)
    dataframe = load_dataframe(filename)
    with pytest.raises(ValueError):
        validate_dataframe(dataframe)
    remove_file(filename)


def test_3():
    """
    Test 3

    Test detect invalid csv: wrong type 1 column
    """
    filename = "text_csv.csv"
    args = CreateCsvColumnsDtypesArgs(
        filename,
        5,
        40,
        {
            0: "int",
            1: "float64",
            2: "float64",
            3: "float64",
            4: "float64"
        }
    )
    create_csv_columns_dtypes(args)
    dataframe = load_dataframe(filename)
    with pytest.raises(ValueError):
        validate_dataframe(dataframe)
    remove_file(filename)


def test_4():
    """
    Test 4

    Test detect invalid csv: wrong type 2+ columns
    """
    filename = "text_csv.csv"
    args = CreateCsvColumnsDtypesArgs(
        filename,
        5,
        40,
        {
            0: "int",
            1: "int",
            2: "str",
            3: "float64",
            4: "float64"
        }
    )
    create_csv_columns_dtypes(args)
    dataframe = load_dataframe(filename)
    with pytest.raises(ValueError):
        validate_dataframe(dataframe)
    remove_file(filename)
