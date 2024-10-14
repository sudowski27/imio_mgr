"""version 0.1.1"""
from .src.load_configuration import load_configuration


def main() -> None:
    """
    Main function
    """
    configure_file = "configuration.json"
    configuration = load_configuration(configure_file)


if __name__ == "__main__":
    main()
