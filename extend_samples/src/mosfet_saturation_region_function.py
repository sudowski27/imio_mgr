"""version 0.1.0"""
from dataclasses import dataclass
from .get_carrier_mobility import get_carrier_mobility
from .const_values import T_0
from .const_values import GATE_TO_SOURCE_VOLTAGE_INDEX, DRAIN_TO_SOURCE_VOLTAGE_INDEX, WIDTH_INDEX


def arguments_unpack(arguments: tuple) -> tuple:
    """
    Get specified values from tuple

    Parameters
    ----------
    arguments: tuple

    Returns
    -------
    tuple
    """
    gate_to_source_voltage_value = arguments[GATE_TO_SOURCE_VOLTAGE_INDEX]
    drain_to_source_voltage_value = arguments[DRAIN_TO_SOURCE_VOLTAGE_INDEX]
    width_value = arguments[WIDTH_INDEX]

    return gate_to_source_voltage_value, drain_to_source_voltage_value, width_value


@dataclass
class MosCoeff:
    """
    Class with coeffs of MOS

    Parameters
    ----------
    mu_0: float
    alpha: float
    c_ox: float
    lambda_coeff: float
    v_th: float
    """
    mu_0: float
    alpha: float
    c_ox: float
    lambda_coeff: float
    v_th: float


@dataclass
class MosfetSaturationRegionFunctionArguments:
    """
    Class with arguments for function
    mosfet_saturation_region_function

    Parameters
    ----------
    arguments: tuple
    t: float
    l: float
    mos_coeffs: MosCoeff
    """
    arguments: tuple
    t: float
    l: float
    mos_coeffs: MosCoeff


def mosfet_saturation_region_function(arguments: MosfetSaturationRegionFunctionArguments):
    """
    Get value of drain current MOS transistor in saturation range

    formula:
    I_d = 1/2 * mu_n * c_ox * w / l * (v_gs - v_th)^2 * (1 + lambda_coeff * v_ds)

    Parameters
    ----------
    arguments: MosfetSaturationRegionFunctionArguments

    Returns
    -------
    float
    """
    mu_n = get_carrier_mobility(arguments.mos_coeffs.mu_0, T_0, arguments.t, arguments.mos_coeffs.alpha)
    v_gs, v_ds, w = arguments_unpack(arguments.arguments)

    i_d = (1.0 / 2.0 * mu_n * arguments.mos_coeffs.c_ox * w / arguments.l *
          pow((v_gs - arguments.mos_coeffs.v_th), 2) *
          (1 + arguments.mos_coeffs.lambda_coeff * v_ds))

    return i_d
