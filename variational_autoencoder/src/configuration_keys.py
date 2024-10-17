"""version 0.1.1"""
from collections import namedtuple


ConfigurationKeys = namedtuple(
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

configuration_keys = ConfigurationKeys(
    "train_dataset_file",
    "test_dataset_file",
    "trained_vae_file_name",
    "synth_data_folder",
    "synth_data_file_name_core",
    "batch_size",
    "epochs",
    "learning_rate",
    "wkl",
    "device"
)
