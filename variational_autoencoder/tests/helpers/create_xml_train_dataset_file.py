"""version 0.1.0"""
import random
from dataclasses import dataclass
import pandas as pd


@dataclass
class CreateXmlTrainDatasetFileArguments:
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


def create_xml_train_dataset_file(args: CreateXmlTrainDatasetFileArguments) -> pd.DataFrame:
    """
    Create xml file with data from dataset.
    width_dim, v_gs_dim, v_ds_dim are number of combinations per device of values.
    device_width_separated is boolen value, and if is true, new value of width will
    be seperated by diffrent device for example:
    dev1 width1
    dev2 width1
    dev1 width2
    dev2 width2

    Parameters
    ----------
    args: CreateXmlTrainDatasetFileArguments
    """
    if args.device_width_separated:
        dataframe = create_train_dataset_dataframe_device_width_seperated(
            args.number_of_devices,
            args.width_dim,
            args.v_gs_dim,
            args.v_ds_dim
        )
    else:
        dataframe = create_train_dataset_dataframe_device_width_together(
            args.number_of_devices,
            args.width_dim,
            args.v_gs_dim,
            args.v_ds_dim
        )
    dataframe.to_csv(args.filename, sep=" ", index=False, header=False)

    return create_train_dataset_dataframe_device_width_together(
            args.number_of_devices,
            args.width_dim,
            args.v_gs_dim,
            args.v_ds_dim
        )


def create_train_dataset_dataframe_device_width_seperated(number_of_devices: int,  # pylint: disable=R0914
                                                          width_dim: int, v_gs_dim:
                                                          int, v_ds_dim: int) -> pd.DataFrame:
    """
    Create dataset with devices seperated

    Parameters
    ----------
    number_of_devices: int
    width_dim: int
    v_gs_dim: int
    v_ds_dim: int
    """
    width_value_min_max = (100, 1000)
    v_gs_min_max = (0.1, 1.1)
    v_ds_min_max = (0.1, 1.1)
    i_d_min_max = (0.0, 0.2)

    width_values = [random.randint(width_value_min_max[0], width_value_min_max[1]) for _ in range(width_dim)]
    v_gs_values = [random.uniform(v_gs_min_max[0], v_gs_min_max[1]) for _ in range(v_gs_dim)]
    v_ds_values = [random.uniform(v_ds_min_max[0], v_ds_min_max[1]) for _ in range(v_ds_dim)]

    data = []
    for width in width_values:
        for device in range(1, number_of_devices + 1):
            for v_gs in v_gs_values:
                for v_ds in v_ds_values:
                    i_d = random.uniform(i_d_min_max[0], i_d_min_max[1])
                    sample = [device, width, v_gs, v_ds, i_d]
                    data.append(sample)

    return pd.DataFrame(data)


def create_train_dataset_dataframe_device_width_together(number_of_devices: int, width_dim: int,  # pylint: disable=R0914  # noqa
                                                         v_gs_dim: int, v_ds_dim: int) -> pd.DataFrame:
    """
    Create dataset with devices seperated

    Parameters
    ----------
    number_of_devices: int
    width_dim: int
    v_gs_dim: int
    v_ds_dim: int
    """
    width_value_min_max = (100, 1000)
    v_gs_min_max = (0.1, 1.1)
    v_ds_min_max = (0.1, 1.1)
    i_d_min_max = (0.0, 0.2)

    width_values = [random.randint(width_value_min_max[0], width_value_min_max[1]) for _ in range(width_dim)]
    v_gs_values = [random.uniform(v_gs_min_max[0], v_gs_min_max[1]) for _ in range(v_gs_dim)]
    v_ds_values = [random.uniform(v_ds_min_max[0], v_ds_min_max[1]) for _ in range(v_ds_dim)]

    data = []
    for device in range(1, number_of_devices + 1):
        for width in width_values:
            for v_gs in v_gs_values:
                for v_ds in v_ds_values:
                    i_d = random.uniform(i_d_min_max[0], i_d_min_max[1])
                    sample = [device, width, v_gs, v_ds, i_d]
                    data.append(sample)

    return pd.DataFrame(data)
