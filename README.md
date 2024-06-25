# Keylogger

## Overview

The Keylogger project is a Python-based tool designed to monitor and record keystrokes on a computer system. This tool captures keyboard input from users and logs the keystrokes, providing insights into user activity for various purposes such as debugging, forensic analysis, or parental control (Note: Ensure legal compliance and ethical considerations before use).

## Features

- Captures keystrokes from the keyboard input.
- Logs keystrokes with timestamps and application context.
- Supports running in stealth mode for discreet operation.
- Saves logs locally or sends them to a specified server.
- Optionally filters and encrypts captured keystrokes for privacy.
- User-friendly command-line interface (CLI) for configuration and operation.

## Requirements

- Python 3.x
- `pynput` library for keyboard monitoring
- `pyinstaller` (optional) for creating standalone executables
- `pycrypto` (optional) for encryption (if needed)

## Installation

1. Clone the repository:
    ```bash
    https://github.com/Aravjnth/Keylogger.git
    cd keylogger
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the keylogger:
    ```bash
    python keylogger.py
    ```

2. Stop the keylogger using a predefined key combination (e.g., `Ctrl + Alt + K`).

3. Access the generated logs in the specified output file or server.

### Example

Start the keylogger:
```bash
python keylogger.py
```

Stop the keylogger using the predefined key combination (`Ctrl + Alt + K`).

## Options

- Customize keylogger settings in `config.py`, such as log file location and encryption options.
- Implement additional features like remote command and control (C2) for sending logs to a remote server.

## Legal Disclaimer

This Keylogger tool is intended for educational and authorized monitoring purposes. Ensure compliance with legal regulations and obtain appropriate consent before deploying such tools. Misuse for unauthorized or malicious activities is strictly prohibited. The developers assume no liability for any misuse or damage caused by this application.

## Contributing

Contributions to this project are welcome! Fork the repository, enhance functionality, improve performance, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, please contact me at www.linkedin.com/in/aravinth-aj
