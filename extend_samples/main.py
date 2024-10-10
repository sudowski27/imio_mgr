"""version 0.1.0"""
import matplotlib.pyplot as plt
from src.load_config import load_config
from src.load_all_source_files import load_all_source_files
from src.load_csv_file import load_csv_file
from src.split_csv_object_by_device import split_csv_object_by_device
from src.get_config_for_csv import get_config_for_csv
from src.get_config_for_device import get_config_for_device
from src.get_device_number import get_device_number
from src.get_channel_width_for_csv import get_channel_width_for_csv
from src.get_coeffs_for_current_device import get_coeffs_for_current_device
from src.get_plot_for_pdf import get_plot_for_pdf
from src.get_pdf_pages import get_pdf_pages
from src.generate_new_device_dataframes import (
    generate_new_device_dataframes,
    GenerateNewDeviceDataframesArguments
)
from src.concatenate_device_dataframes import concatenate_device_dataframes
from src.get_csv_filename import get_csv_filename
from src.save_dataframe_to_csv import save_dataframe_to_csv
from src.join_channel_width_to_device_dataframe import join_channel_width_to_device_dataframe
from src.get_dataframe_with_headers import get_dataframe_with_headers


def main() -> None:
    """
    Main function for extend samples
    """
    config_file = "config.ini"
    config = load_config(config_file)
    source_files = load_all_source_files(config)

    for path_name, path_value in source_files.items():
        print(path_value)
        csv_object = load_csv_file(path_value)
        csv_config_dict = get_config_for_csv(config, path_name)
        splited_csv_object = split_csv_object_by_device(csv_object)

        channel_width = get_channel_width_for_csv(config, path_name)

        pdf = get_pdf_pages(path_name + ".pdf")
        devices_list = []
        last_device_number = 1

        for device in splited_csv_object:
            device_number = get_device_number(device)
            device_config = get_config_for_device(csv_config_dict, device_number)

            print(f"dev number: {device_number}")
            device_coeffs = get_coeffs_for_current_device(device, channel_width)

            generated_plot = get_plot_for_pdf(
                device_coeffs,
                device_number,
                device,
                channel_width
            )
            pdf.savefig()
            plt.close()

            device = join_channel_width_to_device_dataframe(device, channel_width)

            devices_list, last_device_number = generate_new_device_dataframes(
                GenerateNewDeviceDataframesArguments(
                    devices_list,
                    device_config,
                    device,
                    last_device_number,
                    device_coeffs,
                    channel_width
                )
            )

        concatenaded_devices_dataframe = concatenate_device_dataframes(devices_list)

        concatenaded_devices_dataframe = get_dataframe_with_headers(concatenaded_devices_dataframe)
        destination_filename = get_csv_filename(config, path_name)

        save_dataframe_to_csv(
            concatenaded_devices_dataframe,
            destination_filename
        )

        pdf.close()


if __name__ == "__main__":
    main()
