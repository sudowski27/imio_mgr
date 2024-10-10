"""version 0.1.0"""
from .mosfet_saturation_region_function import (
    mosfet_saturation_region_function,
    MosCoeff,
    MosfetSaturationRegionFunctionArguments
)
from .mosfet_linear_region_function import (
    mosfet_linear_region_function,
    MosfetLinearRegionFunctionArguments
)

def mosfet_function(arguments: tuple, mu_0: float, t: float, alpha: float,  # pylint: disable=R0913, R0917
                    c_ox: float, l: float, lambda_coeff: float,
                    v_th: float, a: float, b: float) -> float:
    """
    Get value of drain current MOS transistor

    formula:
    I_d = a * mosfet_saturation_region_function() + b * mosfet_linear_region_function()

    Parameters
    ----------
    arguments: tuple
    mu_0: float
    t: float
    alpha: float
    c_ox: float
    l: float
    lambda_coeff: float
    v_th: float
    a: float
    b: float

    Returns
    -------
    float
    """
    mosfet_linear_arguments = MosfetLinearRegionFunctionArguments(
        arguments,
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
    mosfet_saturation_arguments = MosfetSaturationRegionFunctionArguments(
        arguments,
        t,
        l,
        mos_coeff
    )
    saturation_part = a * mosfet_saturation_region_function(mosfet_saturation_arguments)
    linear_part = b * mosfet_linear_region_function(mosfet_linear_arguments)

    return saturation_part + linear_part
