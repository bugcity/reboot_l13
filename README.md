# Speed Wi-Fi HOME 5G L13 Reboot Python Script

## Overview

This Python script provides a simple way to restart the Speed Wi-Fi HOME 5G L13 device. Restarting the device can be useful in resolving connectivity issues and ensuring optimal performance.

## Prerequisites

Before using this script, make sure you have the following:

- Python installed on your system
- Access to the Speed Wi-Fi HOME 5G L13 device

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/bugcity/reboot_l13.git
    ```

1. Navigate to the project directory:

    ```bash
    cd reboot_l13
    ```

1. Install poetry

    ```bash
    poetry install
    ```

1. Configuration

    Modify the `config.ini` file to match your environment. Update the following parameters:

    ```ini
    [ZTE]
    host = 192.168.0.1
    password = Your_Speed_WiFi_Password
    ```

1. Run the script:

    ```bash
    poetry run python src/reboot_l13.py
    ```

## Important Note

Ensure that you have the necessary permissions and access rights to restart the Speed Wi-Fi HOME 5G L13 device.

Feel free to customize the script according to your needs.

## Contributing

If you encounter issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit).
