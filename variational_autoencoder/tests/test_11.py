"""version 0.1.1"""
import pytest
from variational_autoencoder.src.data_dimensions import load_dataframe
from .helpers.create_csv_train_dataset_file import create_csv_train_dataset_file, CreateCsvTrainDatasetFileArguments
from .helpers.remove_file import remove_file
from .helpers.create_empty_csv_file import create_empty_csv_file


def test_0():
    """
    Test 0

    Test load data from csv
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
    load_dataframe(filename)
    remove_file(filename)


def test_1():
    """
    Test 1

    Test load data from non existing csv
    """
    filename = "text_csv.csv"
    with pytest.raises(FileNotFoundError):
        load_dataframe(filename)


def test_2():
    """
    Test 2

    Test load data from empty csv
    """
    filename = "text_csv.csv"
    create_empty_csv_file(filename)
    with pytest.raises(ValueError):
        load_dataframe(filename)
