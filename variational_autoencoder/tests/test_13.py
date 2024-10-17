"""version 0.1.0"""
from variational_autoencoder.src.data_dimensions import (
    load_dataframe,
    validate_dataframe,
    is_devices_seperated
)
from .helpers.remove_file import remove_file
from .helpers.create_csv_train_dataset_file import create_csv_train_dataset_file, CreateCsvTrainDatasetFileArguments


def test_0():
    """
    Test 0

    Test detect seperated_devices in csv
    """
    filename = "text_csv.csv"
    is_devices_seperated_expected = True
    args = CreateCsvTrainDatasetFileArguments(
        "text_csv.csv",
        5,
        2,
        5,
        5,
        is_devices_seperated_expected
    )
    create_csv_train_dataset_file(args)
    dataframe = load_dataframe(filename)
    validate_dataframe(dataframe)
    assert is_devices_seperated(dataframe) == is_devices_seperated_expected
    remove_file(filename)


def test_1():
    """
    Test 1

    Test detect devices together in csv
    """
    filename = "text_csv.csv"
    is_devices_seperated_expected = False
    args = CreateCsvTrainDatasetFileArguments(
        "text_csv.csv",
        5,
        2,
        5,
        5,
        is_devices_seperated_expected
    )
    create_csv_train_dataset_file(args)
    dataframe = load_dataframe(filename)
    validate_dataframe(dataframe)
    assert is_devices_seperated(dataframe) == is_devices_seperated_expected
    remove_file(filename)
