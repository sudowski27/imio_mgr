"""version 0.1.0"""
from .configuration_keys import configuration_keys
from .configuration_values import configuration_values


def validate_train_dataset_file(configuration: dict) -> None:
    """
    Function validate train_dataset_file part of configuration

    Parameters
    ----------
    configuration: dict

    Raises
    ------
    ValueError
        Error if train_dataset_file key missing
    """
    if configuration.get(configuration_keys.train_dataset_file) is not None:
        if not isinstance(configuration[configuration_keys.train_dataset_file],
                          configuration_values.train_dataset_file):
            raise ValueError(
                f"Value: {configuration_keys.train_dataset_file} is not {configuration_values.train_dataset_file}"
            )
    else:
        raise ValueError(
                f"Missing {configuration_keys.train_dataset_file} key"
            )


def validate_configuration(configuration: dict) -> None:
    """
    Function validate keys of configuration dictionary.
    If configuration is good do nothing, otherwise raise
    exception

    Parameters
    ----------
    configuration: dict

    Raises
    ------
    ValueError
        Error if some keys missing
    """
    pass
