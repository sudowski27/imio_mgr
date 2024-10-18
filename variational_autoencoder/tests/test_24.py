"""version 0.1.0"""
from variational_autoencoder.src.configuration_keys import configuration_keys
from variational_autoencoder.src.get_train_dataframe import get_train_dataframe
from .helpers.create_csv_train_dataset_file import create_csv_train_dataset_file, CreateCsvTrainDatasetFileArguments
from .helpers.remove_file import remove_file


def test_0(small_configure_with_train_dataset_file):
    """
    Test 0

    Test load train dataframe with devices together
    """
    configure = small_configure_with_train_dataset_file
    filemame = configure[configuration_keys.train_dataset_file]
    args = CreateCsvTrainDatasetFileArguments(
        filemame,
        5,
        4,
        10,
        20,
        True
    )
    expected_dataframe = create_csv_train_dataset_file(args)

    train_dataframe = get_train_dataframe(configure)

    assert train_dataframe.equals(expected_dataframe)
    remove_file(filemame)
