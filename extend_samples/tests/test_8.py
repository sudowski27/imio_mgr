"""version 0.1.0"""
from extend_samples.src.mosfet_linear_region_function import (
    mosfet_linear_region_function,
    MosfetLinearRegionFunctionArguments
)
from extend_samples.src.mosfet_saturation_region_function import (
    mosfet_saturation_region_function,
    MosCoeff,
    MosfetSaturationRegionFunctionArguments
)
from extend_samples.src.mosfet_function import mosfet_function


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

    a = 2
    b = 4

    args = (v_gs, v_ds, w)

    linear_mosfet_arguments = MosfetLinearRegionFunctionArguments(
        args,
        mu_0,
        t,
        alpha,
        c_ox,
        l,
        v_th
    )
    mos_coeff = MosCoeff(
        mu_0,
        alpha,
        c_ox,
        lambda_coeff,
        v_th
    )
    saturation_mosfet_arguments = MosfetSaturationRegionFunctionArguments(
        args,
        t,
        l,
        mos_coeff
    )

    expected_value = a * mosfet_saturation_region_function(
                     saturation_mosfet_arguments) + b * mosfet_linear_region_function(
                     linear_mosfet_arguments)

    result = mosfet_function(args, mu_0, t, alpha, c_ox, l, lambda_coeff, v_th, a, b)

    delta = 1e-6

    assert abs(expected_value - result) <= delta
