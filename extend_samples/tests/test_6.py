"""version 0.1.0"""
from extend_samples.src.get_carrier_mobility import get_carrier_mobility
from extend_samples.src.mosfet_saturation_region_function import (
    mosfet_saturation_region_function,
    MosCoeff,
    MosfetSaturationRegionFunctionArguments
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
    lambda_coeff = 1.1
    v_th = 0.5

    args = (v_gs, v_ds, w)

    mu = get_carrier_mobility(mu_0, t_0, t, alpha)

    expected_value = 1 / 2 * mu * c_ox * w / l * pow(v_gs - v_th, 2) * (1 + lambda_coeff  * v_ds)

    mos_coeff = MosCoeff(
        mu_0,
        alpha,
        c_ox,
        lambda_coeff,
        v_th
    )
    arguments = MosfetSaturationRegionFunctionArguments(
        args,
        t,
        l,
        mos_coeff
    )
    result = mosfet_saturation_region_function(arguments)

    delta = 1e-6

    assert abs(result - expected_value) <= delta
