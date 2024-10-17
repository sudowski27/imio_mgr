"""version 0.1.0"""
from variational_autoencoder.src.data_dimensions import (
    load_dataframe,
    validate_dataframe,
    is_devices_seperated,
    connect_devices
)
from .helpers.create_csv_train_dataset_file import create_csv_train_dataset_file, CreateCsvTrainDatasetFileArguments
from .helpers.remove_file import remove_file


def test_0():
    """
    Test 0

    Test connecting devices
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
    dataframe_together = create_csv_train_dataset_file(args)
    dataframe = load_dataframe(filename)
    validate_dataframe(dataframe)

    assert is_devices_seperated(dataframe)
    connected_devices_dataframe = connect_devices(dataframe)
    remove_file(filename)

    assert connected_devices_dataframe.equals(dataframe_together)
