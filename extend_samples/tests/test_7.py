"""version 0.1.0"""
from extend_samples.src.get_carrier_mobility import get_carrier_mobility
from extend_samples.src.mosfet_linear_region_function import (
    mosfet_linear_region_function,
    MosfetLinearRegionFunctionArguments
)


def test_0():
    """
    Test 0

    Test calculate drain current
    """
    v_gs = 1.0
    v_ds = 1.1
    w = 2.0
    mu_0 = 2.0
    t_0 = 300.0
    t = 400.0
    alpha = 2.0
    c_ox = 1e-1
    l = 0.1
    v_th = 0.5

    args = (v_gs, v_ds, w)

    mu = get_carrier_mobility(mu_0, t_0, t, alpha)

    expected_value = 1 / 2 * mu * c_ox * w / l * ((v_gs - v_th) * v_ds - pow(v_ds, 2) / 2)

    arguments = MosfetLinearRegionFunctionArguments(
        args,
        mu_0,
        t,
        alpha,
        c_ox,
        l,
        v_th
    )
    result = mosfet_linear_region_function(arguments)

    delta = 1e-6

    assert abs(result - expected_value) <= delta
