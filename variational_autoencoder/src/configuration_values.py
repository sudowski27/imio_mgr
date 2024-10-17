"""version 0.1.1"""
from collections import namedtuple


ConfigurationValues = namedtuple(
    "ConfigurationKeys",
    ["train_dataset_file",
     "test_dataset_file",
     "trained_vae_file_name",
     "synth_data_folder",
     "synth_data_file_name_core",
     "batch_size",
     "epochs",
     "learning_rate",
     "wkl",
     "device"
     ]
)

configuration_values = ConfigurationValues(
    str,
    str,
    str,
    str,
    str,
    int,
    int,
    float,
    float,
    ["cuda", "cpu"]
)
