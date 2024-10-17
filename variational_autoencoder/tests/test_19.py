"""version 0.1.0"""
from variational_autoencoder.src.data_dimensions import (
    data_dimensions
)
from .helpers.create_csv_train_dataset_file import create_csv_train_dataset_file, CreateCsvTrainDatasetFileArguments
from .helpers.remove_file import remove_file


def test_0():
    """
    Test 0

    Test getting dim with devices together
    """
    filename = "text_csv.csv"
    channel_width_dim_expected = 2
    gate_source_dim_expected = 10
    drain_source_dim_expected = 20
    args = CreateCsvTrainDatasetFileArguments(
        "text_csv.csv",
        40,
        channel_width_dim_expected,
        gate_source_dim_expected,
        drain_source_dim_expected,
        False
    )
    create_csv_train_dataset_file(args)

    channel_width_dim, gate_source_dim, drain_source_dim = data_dimensions(filename)

    assert channel_width_dim == channel_width_dim_expected
    assert gate_source_dim == gate_source_dim_expected
    assert drain_source_dim == drain_source_dim_expected

    remove_file(filename)


def test_1():
    """
    Test 1

    Test getting dim with devices seperated
    """
    filename = "text_csv.csv"
    channel_width_dim_expected = 2
    gate_source_dim_expected = 10
    drain_source_dim_expected = 20
    args = CreateCsvTrainDatasetFileArguments(
        "text_csv.csv",
        40,
        channel_width_dim_expected,
        gate_source_dim_expected,
        drain_source_dim_expected,
        True
    )
    create_csv_train_dataset_file(args)

    channel_width_dim, gate_source_dim, drain_source_dim = data_dimensions(filename)

    assert channel_width_dim == channel_width_dim_expected
    assert gate_source_dim == gate_source_dim_expected
    assert drain_source_dim == drain_source_dim_expected

    remove_file(filename)
