"""version 0.1.0"""
import json


def load_configuration(configuraion_filename: str) -> dict:
    """
    Load config from json file

    Parameters
    ----------
    configuraion_filename: str

    Returns
    -------
    dict

    Raises
    ------
    ValueError
        Json file syntax error
    """
    with open(configuraion_filename, encoding="utf-8") as config:
        try:
            config_dict = json.load(config)
        except json.JSONDecodeError as exc:
            raise ValueError("Please fix JSON file") from exc

    return config_dict
