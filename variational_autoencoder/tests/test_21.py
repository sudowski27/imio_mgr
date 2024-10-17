"""version 0.1.0"""
from unittest import mock
from variational_autoencoder.src.const_values import (
    CPU_DEVICE,
    CUDA_DEVICE
)
from variational_autoencoder.src.get_device import get_device


def test_0(small_configure_with_device_cpu):
    """
    Test 0

    Test configuration with device CPU
    """
    configure = small_configure_with_device_cpu
    expected_device = CPU_DEVICE
    device = get_device(configure)

    assert device == expected_device


def test_1(small_configure_with_device_cuda):
    """
    Test 1

    Test configuration with device CUDA
    """
    configure = small_configure_with_device_cuda
    expected_device = CUDA_DEVICE
    device = get_device(configure)

    assert device == expected_device


def test_2(small_configure_with_device_cuda):
    """
    Test 1

    Test configuration with device CUDA
    and CUDA is not available
    """
    configure = small_configure_with_device_cuda
    expected_device = CPU_DEVICE

    with mock.patch("torch.cuda.is_available", return_value=False):
        device = get_device(configure)

    assert device == expected_device
