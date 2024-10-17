"""version 0.1.1"""
from variational_autoencoder.src.data_dimensions import (
    load_dataframe,
    validate_dataframe,
    is_devices_seperated,
    connect_devices,
    get_first_device,
    count_unique_gate_source_voltages
)
from .helpers.create_csv_train_dataset_file import create_csv_train_dataset_file, CreateCsvTrainDatasetFileArguments
from .helpers.remove_file import remove_file


def test_0():
    """
    Test 0

    Test connecting devices
    """
    filename = "text_csv.csv"
    count_unique_gate_source_voltages_expected = 20
    args = CreateCsvTrainDatasetFileArguments(
        "text_csv.csv",
        5,
        4,
        count_unique_gate_source_voltages_expected,
        5,
        True
    )
    create_csv_train_dataset_file(args)
    dataframe = load_dataframe(filename)
    validate_dataframe(dataframe)

    assert is_devices_seperated(dataframe)
    connected_devices_dataframe = connect_devices(dataframe)
    first_device_dataframe = get_first_device(connected_devices_dataframe)
    count_unique_gate_source_voltages_value = count_unique_gate_source_voltages(first_device_dataframe)
    assert count_unique_gate_source_voltages_value == count_unique_gate_source_voltages_expected
    remove_file(filename)
