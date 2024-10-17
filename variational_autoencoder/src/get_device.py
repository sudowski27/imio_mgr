"""version 0.1.0"""
import torch
from .configuration_keys import configuration_keys
from .const_values import (
    CUDA_DEVICE,
    CPU_DEVICE
)


def get_device(configuration: dict) -> str:
    """
    Get device for torch and check its available

    Parameters
    ----------
    configuration: dict

    Returns
    -------
    str
    """
    device_from_configuration = configuration[configuration_keys.device]
    if device_from_configuration == CUDA_DEVICE:
        if not torch.cuda.is_available():
            device_from_configuration = CPU_DEVICE

    return device_from_configuration
