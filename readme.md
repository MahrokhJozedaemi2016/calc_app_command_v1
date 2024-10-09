# Calculator Command Project

## Description
This project is an interactive command-line calculator application. It allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division, and it keeps a history of calculations. Additionally, the application is built with extensibility in mind, supporting plugins for new operations and incorporating multiprocessing features for enhanced performance.

## Features
- Supports basic arithmetic operations (addition, subtraction, multiplication, division).
- **Menu option** to view available commands and features.
- Interactive command-line interface.
- History management to store and clear calculation records.
- Plugin support for easy extension of operations.
- Multiprocessing for parallel command execution.

## Installation
To install and run the project, clone the repository and install the dependencies:

```bash
git clone https://github.com/MahrokhJozedaemi2016/calc_app_command_v1.git
cd calc_app_command_v1
pip install -r requirements.txt

## Usage
Run python3 main.py

## Runnig Tests
pytest --cov=calculator --cov-report=term-missing
pytest --cov=tests --cov-report=term-missing


