"""version 0.1.2"""
import random
from dataclasses import dataclass
import pandas as pd
from variational_autoencoder.src.const_values import CSV_SEPERATOR


@dataclass
class CreateCsvTrainDatasetFileArguments:
    """
    Parameters
    ----------
    filename: str
    number_of_devices: int
    width_dim: int
    v_gs_dim: int
    v_ds_dim: int
    device_width_separated: bool
    """
    filename: str
    number_of_devices: int
    width_dim: int
    v_gs_dim: int
    v_ds_dim: int
    device_width_separated: bool


def create_csv_train_dataset_file(args: CreateCsvTrainDatasetFileArguments) -> pd.DataFrame:
    """
    Create csv file with data from dataset.
    width_dim, v_gs_dim, v_ds_dim are number of combinations per device of values.
    device_width_separated is boolen value, and if is true, new value of width will
    be seperated by diffrent device for example:
    dev1 width1
    dev2 width1
    dev1 width2
    dev2 width2

    Parameters
    ----------
    args: CreateCsvTrainDatasetFileArguments

    Returns
    -------
    pd.DataFrame
    """
    if args.device_width_separated:
        (dataframe, width_values, v_gs_values,
         v_ds_values, i_d_values) = create_train_dataset_dataframe_device_width_seperated(
            args.number_of_devices,
            args.width_dim,
            args.v_gs_dim,
            args.v_ds_dim
        )
    else:
        (dataframe, width_values, v_gs_values,
         v_ds_values, i_d_values) = create_train_dataset_dataframe_device_width_together(
            args.number_of_devices,
            args.width_dim,
            args.v_gs_dim,
            args.v_ds_dim
        )
    dataframe.to_csv(args.filename, sep=CSV_SEPERATOR, index=False, header=False)

    return create_train_dataset_dataframe_device_width_together_clone(
            args.number_of_devices,
            width_values,
            v_gs_values,
            v_ds_values,
            i_d_values
        )


def create_train_dataset_dataframe_device_width_seperated(number_of_devices: int,  # pylint: disable=R0914
                                                          width_dim: int, v_gs_dim:
                                                          int, v_ds_dim: int) -> tuple:
    """
    Create dataset with devices seperated

    Parameters
    ----------
    number_of_devices: int
    width_dim: int
    v_gs_dim: int
    v_ds_dim: int

    Returns
    -------
    tuple
        (pd.DataFrame, width_values: list, v_gs_values: list, v_ds_values: list, i_d_values: dict)
    """
    width_value_min_max = (100, 1000)
    v_gs_min_max = (0.1, 1.1)
    v_ds_min_max = (0.1, 1.1)
    i_d_min_max = (0.0, 0.2)

    width_values = [random.randint(width_value_min_max[0], width_value_min_max[1]) for _ in range(width_dim)]

    v_gs_values = []
    for _ in range(v_gs_dim):
        val = None
        while val in v_gs_values or val is None:
            val = round(random.uniform(v_gs_min_max[0], v_gs_min_max[1]), 4)
        v_gs_values.append(val)

    v_ds_values = []

    for _ in range(v_ds_dim):
        val = None
        while val in v_ds_values or val is None:
            val = round(random.uniform(v_ds_min_max[0], v_ds_min_max[1]), 4)
        v_ds_values.append(val)

    i_d_values = {}

    data = []
    for width in width_values:
        for device in range(1, number_of_devices + 1):
            for v_gs in v_gs_values:
                for v_ds in v_ds_values:
                    i_d = round(random.uniform(i_d_min_max[0], i_d_min_max[1]), 4)
                    sample = [device, width, v_gs, v_ds, i_d]
                    data.append(sample)
                    try:
                        i_d_values[str(device)]
                    except KeyError:
                        i_d_values[str(device)] = {}
                    try:
                        i_d_values[str(device)][str(width)]
                    except KeyError:
                        i_d_values[str(device)][str(width)] = {}
                    try:
                        i_d_values[str(device)][str(width)][str(v_gs)]
                    except KeyError:
                        i_d_values[str(device)][str(width)][str(v_gs)] = {}

                    i_d_values[str(device)][str(width)][str(v_gs)][str(v_ds)] = i_d

    return pd.DataFrame(data), width_values, v_gs_values, v_ds_values, i_d_values


def create_train_dataset_dataframe_device_width_together(number_of_devices: int, width_dim: int,  # pylint: disable=R0914  # noqa
                                                         v_gs_dim: int, v_ds_dim: int) -> tuple:
    """
    Create dataset with devices together

    Parameters
    ----------
    number_of_devices: int
    width_dim: int
    v_gs_dim: int
    v_ds_dim: int

    Returns
    -------
    tuple
        (pd.DataFrame, width_values: list, v_gs_values: list, v_ds_values: list, i_d_values: dict)
    """
    width_value_min_max = (100, 1000)
    v_gs_min_max = (0.1, 1.1)
    v_ds_min_max = (0.1, 1.1)
    i_d_min_max = (0.0, 0.2)

    width_values = [round(random.randint(width_value_min_max[0], width_value_min_max[1]), 4) for _ in range(width_dim)]
    v_gs_values = []
    for _ in range(v_gs_dim):
        val = None
        while val in v_gs_values or val is None:
            val = round(random.uniform(v_gs_min_max[0], v_gs_min_max[1]), 4)
        v_gs_values.append(val)

    v_ds_values = []

    for _ in range(v_ds_dim):
        val = None
        while val in v_ds_values or val is None:
            val = round(random.uniform(v_ds_min_max[0], v_ds_min_max[1]), 4)
        v_ds_values.append(val)

    i_d_values = {}

    data = []
    for device in range(1, number_of_devices + 1):
        for width in width_values:
            for v_gs in v_gs_values:
                for v_ds in v_ds_values:
                    i_d = round(random.uniform(i_d_min_max[0], i_d_min_max[1]), 4)
                    sample = [device, width, v_gs, v_ds, i_d]
                    data.append(sample)
                    try:
                        i_d_values[str(device)]
                    except KeyError:
                        i_d_values[str(device)] = {}
                    try:
                        i_d_values[str(device)][str(width)]
                    except KeyError:
                        i_d_values[str(device)][str(width)] = {}
                    try:
                        i_d_values[str(device)][str(width)][str(v_gs)]
                    except KeyError:
                        i_d_values[str(device)][str(width)][str(v_gs)] = {}

                    i_d_values[str(device)][str(width)][str(v_gs)][str(v_ds)] = i_d

    return pd.DataFrame(data), width_values, v_gs_values, v_ds_values, i_d_values


def create_train_dataset_dataframe_device_width_together_clone(number_of_devices: int,
                                                               width_values: list, v_gs_values: list,
                                                               v_ds_values: list, i_d_values: dict) -> pd.DataFrame:
    """
    Create dataset with devices together for check

    Parameters
    ----------
    number_of_devices: int
    width_values: list
    v_gs_values: list
    v_ds_values: list
    i_d_values: dict

    Returns
    -------
    pd.DataFrame
    """
    data = []
    for device in range(1, number_of_devices + 1):
        for width in width_values:
            for v_gs in v_gs_values:
                for v_ds in v_ds_values:
                    i_d = float(i_d_values[str(device)][str(width)][str(v_gs)][str(v_ds)])
                    sample = [device, int(width), float(v_gs), float(v_ds), float(i_d)]
                    data.append(sample)

    return pd.DataFrame(data)
