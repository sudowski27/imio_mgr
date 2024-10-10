"""version 0.1.0"""
from extend_samples.src.mosfet_saturation_region_function import arguments_unpack


def test_0():
    """
    Test 0

    Test unpack values
    """
    value_0 = 1
    value_1 = 2
    value_2 = 3

    expected_value = (value_0, value_1, value_2)
    args = (value_0, value_1, value_2)
    result = arguments_unpack(args)

    assert result == expected_value
