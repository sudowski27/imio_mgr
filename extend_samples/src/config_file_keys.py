"""version 0.1.0"""
from collections import namedtuple


ConfigKeys = namedtuple(
    "ConfigKeys",
    ["source", "destination", "configuration", "channel_width"]
)

config_keys = ConfigKeys(
    "Source",
    "Destination",
    "Configuration",
    "Channel_Width"
)
