"""version 0.1.2"""
from src.load_configuration import load_configuration
from src.validate_configuration import validate_configuration
from src.data_dimensions import data_dimensions
from src.configuration_keys import configuration_keys


def main() -> None:
    """
    Main function
    """
    configure_file = "configuration.json"
    configuration = load_configuration(configure_file)
    validate_configuration(configuration)

    (channel_width_dim,
     gate_source_dim,
     drain_source_dim) = data_dimensions(configuration[configuration_keys.train_dataset_file])


if __name__ == "__main__":
    main()
