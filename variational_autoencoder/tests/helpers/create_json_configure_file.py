"""version 0.1.0"""
import json
import random
import string


def create_json_configure_file(filename: str, is_json_syntax_good=True) -> dict:
    """
    Creates json file with example configure. If is_json_syntax_good is False,
    some syntax mistake will be add.

    Parameters
    ----------
    filename: str
    is_json_syntax_good: bool = True

    Returns
    -------
    dict
    """
    configure_dict = {
        "train_dataset_file": "../mos_ref_data/nmos_130nm_gaussian_l_vth_rds_50_devs_into_subth.csv",
        "test_dataset_file": "../mos_ref_data/nmos_130nm_gaussian_l_vth_rds_100_devs_into_subth_VALIDATION.csv",
        "trained_vae_file_name": "../pytorch_vaes/vae_nmos_130nm_trained_on_50_devs.pt"
    }

    json_string = json.dumps(configure_dict, indent=4)

    if is_json_syntax_good is False:
        characters = string.ascii_letters + string.digits
        random_string_length = 20
        random_string = "".join(random.choice(characters) for _ in range(random_string_length))

        json_string += random_string

    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(json_string)

    if is_json_syntax_good:
        return configure_dict
    return None
