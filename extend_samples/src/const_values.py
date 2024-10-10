"""version 0.1.0"""
import numpy as np


DEVICE_INDEX = 0
GATE_TO_SOURCE_VOLTAGE_INDEX_DATA_FRAME = 1
DRAIN_TO_SOURCE_VOLTAGE_INDEX_DATA_FRAME = 2
DRAIN_CURRENT_INDEX_DATA_FRAME = 3
CHANNEL_WIDTH_INDEX_DATA_FRAME = 4
CSV_SEPERATOR = " "
T_0 = 300  # [K]
GATE_TO_SOURCE_VOLTAGE_INDEX = 0
DRAIN_TO_SOURCE_VOLTAGE_INDEX = 1
WIDTH_INDEX = 2
CURVE_FIT_MAX_FEW = 20000
curve_fit_lower_bounds = [0, 0.1, 0.1, -np.inf, -np.inf, -np.inf, -np.inf, -np.inf, -np.inf]
curve_fit_upper_bounds = [np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf, np.inf]

coeffs_indexes = {
    "mu_0": 0,
    "t": 1,
    "alpha": 2,
    "c_ox": 3,
    "l": 4,
    "lambda_coeff": 5,
    "v_th": 6,
    "a": 7,
    "b": 8
}
ORGINAL_VALUES_LEGEND = "orginal"
ORGINAL_VALUES_LINESTYLE = "o"
RECONSTRUCTION_VALUES_LEGEND = "reconstruction"
RECONSTRUCTION_VALUES_LINESTYLE = "X"
PLOT_NROWS_NCOLS_INDEX = 111
PLOT_PROJECTION = '3d'
XLABEL_STR = "$V_{ds}$"
YLABEL_STR = "$V_{gs}$"
ZLABEL_STR = "$I_{ds}$"
