"""version 0.1.0"""
from dataclasses import dataclass
import numpy as np
import pandas as pd
import matplotlib.pyplot
from .get_drain_to_source_voltage_array import get_drain_to_source_voltage_array
from .get_gate_to_source_voltage_array import get_gate_to_source_voltage_array
from .get_drain_current_array import get_drain_current_array
from .get_arguments_tuple import get_arguments_tuple
from .const_values import coeffs_indexes, ORGINAL_VALUES_LEGEND, RECONSTRUCTION_VALUES_LEGEND
from .const_values import ORGINAL_VALUES_LINESTYLE, RECONSTRUCTION_VALUES_LINESTYLE
from .const_values import PLOT_NROWS_NCOLS_INDEX, PLOT_PROJECTION
from .const_values import XLABEL_STR, YLABEL_STR, ZLABEL_STR
from .mosfet_function import mosfet_function


@dataclass
class Coefficients:
    """
    Class with coefficients for MOSFET model

    Parameters
    ----------
    mu_0: float
    t: float
    alpha: float
    c_ox: float
    l: float
    lambda_coeff: float
    v_th: float
    """
    mu_0: float
    t: float
    alpha: float
    c_ox: float
    l: float
    lambda_coeff: float
    v_th: float


@dataclass
class HelperCoefficients:
    """
    class with helper coefficients

    Parameters
    ----------
    a: float
    b: float
    """
    a: float
    b: float


@dataclass
class Arrays:
    """
    Class for help storage arrays
    in function get_plot_for_pdf

    Parameters
    ----------
    x: np.array
    y: np.array
    z_orginal: np.array
    z_reconstruction: np.array
    """
    x: np.array = None
    y: np.array = None
    z_orginal: np.array = None
    z_reconstruction: np.array = None


def get_plot_for_pdf(coeffs: np.array, device_number: int,
                     device_data_frame: pd.DataFrame, channel_width: float) -> tuple:
    """
    Create plot for pdf file

    Parameters
    ----------
    coeffs: np.array
    device_number: int
    device_data_frame: pd.DataFrame
    channel_width: float

    Returns
    -------
    tuple
        (matplotlib.figure.Figure, matplotlib.axes._subplots.AxesSubplot)
    """
    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(PLOT_NROWS_NCOLS_INDEX, projection=PLOT_PROJECTION)
    arrays = Arrays()
    arrays.x = get_drain_to_source_voltage_array(device_data_frame)
    arrays.y = get_gate_to_source_voltage_array(device_data_frame)
    arrays.z_orginal = get_drain_current_array(device_data_frame)

    arrays.z_reconstruction = np.zeros_like(arrays.z_orginal)

    arguments = get_arguments_tuple(device_data_frame, channel_width)

    check_array_shape_indexes = (0, 0)
    array_shape = arguments[check_array_shape_indexes[0]].shape[check_array_shape_indexes[1]]
    for i in range(array_shape):
        argument = (arguments[0][i], arguments[1][i], arguments[2][i])

        coefficients = Coefficients(
            coeffs[coeffs_indexes["mu_0"]],
            coeffs[coeffs_indexes["t"]],
            alpha = coeffs[coeffs_indexes["alpha"]],
            c_ox = coeffs[coeffs_indexes["c_ox"]],
            l = coeffs[coeffs_indexes["l"]],
            lambda_coeff = coeffs[coeffs_indexes["lambda_coeff"]],
            v_th = coeffs[coeffs_indexes["v_th"]]
        )
        helper_coeffs = HelperCoefficients(
            a = coeffs[coeffs_indexes["a"]],
            b = coeffs[coeffs_indexes["b"]]
        )

        arrays.z_reconstruction[i] = mosfet_function(argument, coefficients.mu_0, coefficients.t, coefficients.alpha,
                                                     coefficients.c_ox, coefficients.l, coefficients.lambda_coeff,
                                                     coefficients.v_th, helper_coeffs.a, helper_coeffs.b)

    ax.scatter(arrays.x, arrays.y, arrays.z_orginal, marker=ORGINAL_VALUES_LINESTYLE, label=ORGINAL_VALUES_LEGEND)
    ax.scatter(arrays.x, arrays.y, arrays.z_reconstruction,
               marker=RECONSTRUCTION_VALUES_LINESTYLE, label=RECONSTRUCTION_VALUES_LEGEND)
    ax.legend()
    ax.set_title(f"Device {device_number}")
    ax.set_xlabel(XLABEL_STR)
    ax.set_ylabel(YLABEL_STR)
    ax.set_zlabel(ZLABEL_STR)

    return fig, ax
