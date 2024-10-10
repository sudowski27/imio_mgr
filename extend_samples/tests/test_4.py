"""version 0.1.0"""
import pytest
from extend_samples.src.get_carrier_mobility import get_carrier_mobility


def test_0():
    """
    Test 0

    Test calculate value
    """
    mu_0 = 1.0
    T_0 = 300.0
    T = 350.0
    alpha = 2.0

    delta = 1e-5

    expected_value = mu_0 * pow(T_0 / T, alpha)
    result = get_carrier_mobility(mu_0, T_0, T, alpha)

    assert abs(expected_value - result) <= delta


def test_1():
    """
    Test 1

    Test exception: devide by 0
    """
    mu_0 = 1.0
    T_0 = 300.0
    T = 0.0
    alpha = 2.0

    with pytest.raises(ValueError):
        get_carrier_mobility(mu_0, T_0, T, alpha)
