"""version 0.1.0"""
from collections import namedtuple


DeviceConfigKeys = namedtuple(
    "DeviceConfigKeys",
    ["number_of_cases",
     "cases",
     "channel_length",
     "temperature"
    ]
)

device_config_keys = DeviceConfigKeys(
    "number_of_cases",
    "cases",
    "channel_length",
    "temperature"
)
