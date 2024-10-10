"""version 0.1.0"""
import configparser


def load_config(path: str) -> configparser.ConfigParser:
    """
    Return ConfigParser file

    Parameters
    ----------
    path: str

    Returns
    -------
    configparser.ConfigParser()
    """
    config = configparser.ConfigParser()
    with open(path, encoding="utf8"):
        config.read(path)

    return config
