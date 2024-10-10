"""version 0.1.0"""
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit, Bounds
from .get_arguments_tuple import get_arguments_tuple
from .get_drain_current_array import get_drain_current_array
from .mosfet_function import mosfet_function
from .const_values import (
    CURVE_FIT_MAX_FEW,
    curve_fit_lower_bounds,
    curve_fit_upper_bounds
)


def get_coeffs_for_current_device(device_data_frame: pd.DataFrame, channel_width: float) -> np.array:
    """
    Get coeffs from model and samples

    Parameters
    ----------
    device_data_frame: pd.DataFrame
    channel_width: float

    Returns
    -------
    np.array
    """
    arguments = get_arguments_tuple(device_data_frame, channel_width)
    values = get_drain_current_array(device_data_frame)

    kwargs = {"maxfev": CURVE_FIT_MAX_FEW}

    bounds = Bounds(lb=curve_fit_lower_bounds, ub=curve_fit_upper_bounds)

    popt, *_ = curve_fit(mosfet_function, arguments, values, bounds=bounds, **kwargs)

    return popt
