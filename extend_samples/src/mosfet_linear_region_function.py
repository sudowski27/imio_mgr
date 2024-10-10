"""version 0.1.0"""
from dataclasses import dataclass
from .mosfet_saturation_region_function import arguments_unpack
from .get_carrier_mobility import get_carrier_mobility
from .const_values import T_0


@dataclass
class MosfetLinearRegionFunctionArguments:
    """
    Class with arguments for function
    mosfet_linear_region_function

    Parameters
    ----------
    arguments: tuple
    mu_0: float
    t: float
    alpha: float
    c_ox: float
    l: float
    v_th: float
    """
    arguments: tuple
    mu_0: float
    t: float
    alpha: float
    c_ox: float
    l: float
    v_th: float


def mosfet_linear_region_function(arguments: MosfetLinearRegionFunctionArguments) -> float:
    """
    Get value of drain current MOS transistor in linear range

    formula
    I_d = 1/2 * mu_n * c_ox * w/l * ((v_gs - v_th) * v_ds - 1/2 * v_ds^2)

    Parameters
    ----------
    arguments: MosfetLinearRegionFunctionArguments

    Returns
    -------
    float
    """
    mu_n = get_carrier_mobility(arguments.mu_0, T_0, arguments.t, arguments.alpha)
    v_gs, v_ds, w = arguments_unpack(arguments.arguments)

    i_d = 1 / 2 * mu_n * arguments.c_ox * w / arguments.l * ((v_gs - arguments.v_th) * v_ds - pow(v_ds, 2) / 2)
    return i_d
