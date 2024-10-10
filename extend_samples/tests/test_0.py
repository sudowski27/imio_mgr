"""version 0.1.0"""
from extend_samples.src.split_csv_object_by_device import split_csv_object_by_device
import pandas as pd


def compare_dataframe_lists(list1: list, list2: list) -> None:
    """
    Compare two lists with DataFrames
    """
    if len(list1) != len(list2):
        return False

    for df1, df2 in zip(list1, list2):
        if not df1.equals(df2):
            return False

    return True


def test_0():
    """
    Test 0

    Test split DataFrame with two diffrent devices
    """
    device_1_data = [
        [1, 0.0, 5e-2, 2e-12],
        [1, 0.0, 6e-2, 4e-12]
    ]
    device_2_data = [
        [2, 0.0, 8e-2, 4e-12],
        [2, 0.0, 10e-2, 6e-12]
    ]
    measure_data = device_1_data + device_2_data

    measure_data_frame = pd.DataFrame(measure_data)
    measure_data_frame = measure_data_frame
    device_1_data_frame = pd.DataFrame(device_1_data)
    device_2_data_frame = pd.DataFrame(device_2_data)

    expected_data = [device_1_data_frame, device_2_data_frame]
    result = split_csv_object_by_device(measure_data_frame)

    assert compare_dataframe_lists(expected_data, result)


def test_1():
    """
    Test 1

    Test split DataFrame with one diffrent device
    """
    device_1_data = [
        [1, 0.0, 5e-2, 2e-12],
        [1, 0.0, 6e-2, 4e-12]
    ]

    measure_data = device_1_data

    measure_data_frame = pd.DataFrame(measure_data)
    measure_data_frame = measure_data_frame
    device_1_data_frame = pd.DataFrame(device_1_data)

    expected_data = [device_1_data_frame]
    result = split_csv_object_by_device(measure_data_frame)

    assert compare_dataframe_lists(expected_data, result)


def test_2():
    """
    Test 2

    Test split DataFrame with three diffrent devices
    """
    device_1_data = [
        [1, 0.0, 5e-2, 2e-12],
        [1, 0.0, 6e-2, 4e-12]
    ]
    device_2_data = [
        [2, 0.0, 8e-2, 4e-12],
        [2, 0.0, 10e-2, 6e-12]
    ]
    device_3_data = [
        [3, 0.0, 8e-2, 4e-12],
    ]

    measure_data = device_1_data + device_2_data + device_3_data

    measure_data_frame = pd.DataFrame(measure_data)
    measure_data_frame = measure_data_frame
    device_1_data_frame = pd.DataFrame(device_1_data)
    device_2_data_frame = pd.DataFrame(device_2_data)
    device_3_data_frame = pd.DataFrame(device_3_data)

    expected_data = [device_1_data_frame, device_2_data_frame, device_3_data_frame]
    result = split_csv_object_by_device(measure_data_frame)

    assert compare_dataframe_lists(expected_data, result)
