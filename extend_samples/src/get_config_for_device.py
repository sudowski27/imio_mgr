"""version 0.1.0"""


def get_config_for_device(csv_config: dict, device_number: int) -> dict:
    """
    Get config for one device

    Parameters
    ----------
    csv_config: dict
    device_number: int

    Returns
    -------
    dict

    Raises
    ------
    KeyError
        If device number doesn't exist
    """
    try:
        device_config = csv_config[str(device_number)]
    except KeyError as exc:
        raise KeyError(f"Device {device_number} not found") from exc

    return device_config
