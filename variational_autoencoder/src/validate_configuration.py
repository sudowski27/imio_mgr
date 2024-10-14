"""version 0.1.1"""
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
        Error if train_dataset_file key missing or
        value type is diffrent than expected
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


def validate_test_dataset_file(configuration: dict) -> None:
    """
    Function validate test_dataset_file part of configuration

    Parameters
    ----------
    configuration: dict

    Raises
    ------
    ValueError
        Error if test_dataset_file key missing or
        value type is diffrent than expected
    """
    if configuration.get(configuration_keys.test_dataset_file) is not None:
        if not isinstance(configuration[configuration_keys.test_dataset_file],
                          configuration_values.test_dataset_file):
            raise ValueError(
                f"Value: {configuration_keys.test_dataset_file} is not {configuration_values.test_dataset_file}"
            )
    else:
        raise ValueError(
                f"Missing {configuration_keys.test_dataset_file} key"
            )


def validate_trained_vae_file_name(configuration: dict) -> None:
    """
    Function validate trained_vae_file_name part of configuration

    Parameters
    ----------
    configuration: dict

    Raises
    ------
    ValueError
        Error if trained_vae_file_name key missing or
        value type is diffrent than expected
    """
    if configuration.get(configuration_keys.trained_vae_file_name) is not None:
        if not isinstance(configuration[configuration_keys.trained_vae_file_name],
                          configuration_values.trained_vae_file_name):
            raise ValueError(
                f"Value: {configuration_keys.trained_vae_file_name} is not {configuration_values.trained_vae_file_name}"
            )
    else:
        raise ValueError(
                f"Missing {configuration_keys.trained_vae_file_name} key"
            )


def validate_synth_data_folder(configuration: dict) -> None:
    """
    Function validate synth_data_folder part of configuration

    Parameters
    ----------
    configuration: dict

    Raises
    ------
    ValueError
        Error if synth_data_folder key missing or
        value type is diffrent than expected
    """
    if configuration.get(configuration_keys.synth_data_folder) is not None:
        if not isinstance(configuration[configuration_keys.synth_data_folder],
                          configuration_values.synth_data_folder):
            raise ValueError(
                f"Value: {configuration_keys.synth_data_folder} is not {configuration_values.synth_data_folder}"
            )
    else:
        raise ValueError(
                f"Missing {configuration_keys.synth_data_folder} key"
            )


def validate_synth_data_file_name_core(configuration: dict) -> None:
    """
    Function validate synth_data_file_name_core part of configuration

    Parameters
    ----------
    configuration: dict

    Raises
    ------
    ValueError
        Error if synth_data_file_name_core key missing or
        value type is diffrent than expected
    """
    if configuration.get(configuration_keys.synth_data_file_name_core) is not None:
        if not isinstance(configuration[configuration_keys.synth_data_file_name_core],
                          configuration_values.synth_data_file_name_core):
            raise ValueError(
                (f"Value: {configuration_keys.synth_data_file_name_core} is not "
                 f"{configuration_values.synth_data_file_name_core}")
            )
    else:
        raise ValueError(
                f"Missing {configuration_keys.synth_data_file_name_core} key"
            )


def validate_batch_size(configuration: dict) -> None:
    """
    Function validate batch_size part of configuration

    Parameters
    ----------
    configuration: dict

    Raises
    ------
    ValueError
        Error if batch_size key missing or
        value type is diffrent than expected
    """
    if configuration.get(configuration_keys.batch_size) is not None:
        if not isinstance(configuration[configuration_keys.batch_size],
                          configuration_values.batch_size):
            raise ValueError(
                f"Value: {configuration_keys.batch_size} is not {configuration_values.batch_size}"
            )
    else:
        raise ValueError(
                f"Missing {configuration_keys.batch_size} key"
            )


def validate_learning_rate(configuration: dict) -> None:
    """
    Function validate learning_rate part of configuration

    Parameters
    ----------
    configuration: dict

    Raises
    ------
    ValueError
        Error if learning_rate key missing or
        value type is diffrent than expected
    """
    if configuration.get(configuration_keys.learning_rate) is not None:
        if not isinstance(configuration[configuration_keys.learning_rate],
                          configuration_values.learning_rate):
            raise ValueError(
                f"Value: {configuration_keys.learning_rate} is not {configuration_values.learning_rate}"
            )
    else:
        raise ValueError(
                f"Missing {configuration_keys.learning_rate} key"
            )


def validate_wkl(configuration: dict) -> None:
    """
    Function validate wkl part of configuration

    Parameters
    ----------
    configuration: dict

    Raises
    ------
    ValueError
        Error if wkl key missing or
        value type is diffrent than expected
    """
    if configuration.get(configuration_keys.wkl) is not None:
        if not isinstance(configuration[configuration_keys.wkl],
                          configuration_values.wkl):
            raise ValueError(
                f"Value: {configuration_keys.wkl} is not {configuration_values.wkl}"
            )
    else:
        raise ValueError(
                f"Missing {configuration_keys.wkl} key"
            )


def validate_device(configuration: dict) -> None:
    """
    Function validate device part of configuration

    Parameters
    ----------
    configuration: dict

    Raises
    ------
    ValueError
        Error if device key missing or
        value type is diffrent than expected
    """
    if configuration.get(configuration_keys.device) is not None:
        if not configuration[configuration_keys.device] in configuration_values.device:
            raise ValueError(
                f"Value: {configuration_keys.device} is not {configuration_values.device}"
            )
    else:
        raise ValueError(
                f"Missing {configuration_keys.device} key"
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
    validate_train_dataset_file(configuration)
    validate_test_dataset_file(configuration)
    validate_trained_vae_file_name(configuration)
    validate_synth_data_folder(configuration)
    validate_synth_data_file_name_core(configuration)
    validate_batch_size(configuration)
    validate_learning_rate(configuration)
    validate_wkl(configuration)
    validate_device(configuration)
