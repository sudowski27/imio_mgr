"""version 0.1.0"""
import pytest
from variational_autoencoder.src.data_dimensions import load_dataframe
from .helpers.create_xml_train_dataset_file import create_xml_train_dataset_file, CreateXmlTrainDatasetFileArguments
from .helpers.remove_file import remove_file


def test_0():
    """
    Test 0

    Test load data from csv
    """
    filename = "text_csv.csv"
    args = CreateXmlTrainDatasetFileArguments(
        "text_csv.csv",
        5,
        2,
        5,
        5,
        True
    )
    create_xml_train_dataset_file(args)
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
