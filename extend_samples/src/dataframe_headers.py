"""version 0.1.0"""
from collections import namedtuple


DataFrameHeaders = namedtuple(
    "DataFrameHeaders",
    ["device",
     "v_gs",
     "v_ds",
     "i_d",
     "channel_width"
     ]
)

dataframe_headers = DataFrameHeaders(
    "device",
    "v_gs",
    "v_ds",
    "i_d",
    "channel_width"
)
