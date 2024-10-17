"""version 0.1.2"""
from variational_autoencoder.src.configuration_keys import configuration_keys


def create_configure_dict(**kwargs) -> dict:  # pylint: disable=R0912, R0915
    """
    Create configure dictionary with some errors if its planned.
    If some value in kwargs is true, delete key or change value

    Parameters
    ----------
    **kwargs: dict, optional
        train_dataset_file_key: bool
        train_dataset_file_value: bool
        test_dataset_file_key: bool
        test_dataset_file_value: bool
        trained_vae_file_name_key: bool
        trained_vae_file_name_value: bool
        synth_data_folder_key: bool
        synth_data_folder_value: bool
        synth_data_file_name_core_key: bool
        synth_data_file_name_core_value: bool
        batch_size_key: bool
        batch_size_value: bool
        epochs_key: bool
        epochs_value: bool
        learning_rate_key: bool
        learning_rate_value: bool
        wkl_key: bool
        wkl_value: bool
        device_key : bool
        device_value: bool

    Returns
    -------
    dict
    """
    good_configure_dict = {
        configuration_keys.train_dataset_file: "../mos_ref_data/nmos_130nm_gaussian_l_vth_rds_50_devs_into_subth.csv",
        configuration_keys.test_dataset_file:
            "../mos_ref_data/nmos_130nm_gaussian_l_vth_rds_100_devs_into_subth_VALIDATION.csv",
        configuration_keys.trained_vae_file_name: "./pytorch_vaes/vae_nmos_130nm_trained_on_50_devs.pt",
        configuration_keys.synth_data_folder: "./mosfet_dc_synthetic/trained_on_50",
        configuration_keys.synth_data_file_name_core: "nmos_dc_synth",
        configuration_keys.batch_size: 25,
        configuration_keys.epochs: 40000,
        configuration_keys.learning_rate: 1e-4,
        configuration_keys.wkl: 0.01,
        configuration_keys.device: "cuda"
    }

    if not kwargs:
        return good_configure_dict

    bad_configure_dict = good_configure_dict.copy()

    if "train_dataset_file_key" in kwargs:
        if kwargs["train_dataset_file_key"]:
            bad_configure_dict.pop(configuration_keys.train_dataset_file, None)

    if "train_dataset_file_value" in kwargs:
        if kwargs["train_dataset_file_value"]:
            if configuration_keys.train_dataset_file in bad_configure_dict:
                bad_configure_dict[configuration_keys.train_dataset_file] = 10

    if "test_dataset_file_key" in kwargs:
        if kwargs["test_dataset_file_key"]:
            bad_configure_dict.pop(configuration_keys.test_dataset_file, None)

    if "test_dataset_file_value" in kwargs:
        if kwargs["test_dataset_file_value"]:
            if configuration_keys.test_dataset_file in bad_configure_dict:
                bad_configure_dict[configuration_keys.test_dataset_file] = 10

    if "trained_vae_file_name_key" in kwargs:
        if kwargs["trained_vae_file_name_key"]:
            bad_configure_dict.pop(configuration_keys.trained_vae_file_name, None)

    if "trained_vae_file_name_value" in kwargs:
        if kwargs["trained_vae_file_name_value"]:
            if configuration_keys.trained_vae_file_name in bad_configure_dict:
                bad_configure_dict[configuration_keys.trained_vae_file_name] = 10

    if "synth_data_folder_key" in kwargs:
        if kwargs["synth_data_folder_key"]:
            bad_configure_dict.pop(configuration_keys.synth_data_folder, None)

    if "synth_data_folder_value" in kwargs:
        if kwargs["synth_data_folder_value"]:
            if configuration_keys.synth_data_folder in bad_configure_dict:
                bad_configure_dict[configuration_keys.synth_data_folder] = 10

    if "synth_data_file_name_core_key" in kwargs:
        if kwargs["synth_data_file_name_core_key"]:
            bad_configure_dict.pop(configuration_keys.synth_data_file_name_core, None)

    if "synth_data_file_name_core_value" in kwargs:
        if kwargs["synth_data_file_name_core_value"]:
            if configuration_keys.synth_data_file_name_core in bad_configure_dict:
                bad_configure_dict[configuration_keys.synth_data_file_name_core] = 10

    if "batch_size_key" in kwargs:
        if kwargs["batch_size_key"]:
            bad_configure_dict.pop(configuration_keys.batch_size, None)

    if "batch_size_value" in kwargs:
        if kwargs["batch_size_value"]:
            if configuration_keys.batch_size in bad_configure_dict:
                bad_configure_dict[configuration_keys.batch_size] = "aaa"

    if "epochs_key" in kwargs:
        if kwargs["epochs_key"]:
            bad_configure_dict.pop(configuration_keys.epochs, None)

    if "epochs_value" in kwargs:
        if kwargs["epochs_value"]:
            if configuration_keys.epochs in bad_configure_dict:
                bad_configure_dict[configuration_keys.epochs] = "aaa"

    if "learning_rate_key" in kwargs:
        if kwargs["learning_rate_key"]:
            bad_configure_dict.pop(configuration_keys.learning_rate, None)

    if "learning_rate_value" in kwargs:
        if kwargs["learning_rate_value"]:
            if configuration_keys.learning_rate in bad_configure_dict:
                bad_configure_dict[configuration_keys.learning_rate] = "aaa"

    if "wkl_key" in kwargs:
        if kwargs["wkl_key"]:
            bad_configure_dict.pop(configuration_keys.wkl, None)

    if "wkl_value" in kwargs:
        if kwargs["wkl_value"]:
            if configuration_keys.wkl in bad_configure_dict:
                bad_configure_dict[configuration_keys.wkl] = "aaa"

    if "device_key" in kwargs:
        if kwargs["device_key"]:
            bad_configure_dict.pop(configuration_keys.device, None)

    if "device_value" in kwargs:
        if kwargs["device_value"]:
            if configuration_keys.device in bad_configure_dict:
                bad_configure_dict[configuration_keys.device] = "cuda1"

    return bad_configure_dict
