# Advanced Calculator

This project is an implementation of a calculator capable of performing basic arithmetic operations—addition, subtraction, multiplication, and division—while storing a history of calculations. The project follows Object-Oriented Programming (OOP) principles and is designed with a focus on testing, modularity, and best practices such as SOLID, DRY, and separation of concerns.

## Features
- Basic Operations: Perform addition, subtraction, multiplication, and division.
- Error Handling: Throws exceptions when attempting to divide by zero.
- Calculation History: Stores all calculations and allows users to retrieve or c  lear the history.
- Comprehensive Testing: Fully tested with unit tests and pylint compliance.
- Modular Code: Well-organized with a clear separation of concerns between opera  tions, calculations, and history management.

## Installation
- To set up the Advanced Calculator project on your local machine:
- Clone the repository from GitHub using your preferred method.
- Navigate to the project directory.
- Create a virtual environment (optional but recommended for Python projects).
 Install the required dependencies from the provided requirements.txt file.

## How to Use the Calculator
The calculator offers several arithmetic functions such as addition, subtraction, multiplication, and division. These operations can be performed directly, and the results will be saved in the calculator’s history.

## Basic Operations
The calculator provides methods for performing the following operations:

- Addition: Adds two numbers.
- Subtraction: Subtracts one number from another.
- Multiplication: Multiplies two numbers.
- Division: Divides one number by another, with validation for division by zero.
Each operation is performed using static methods, ensuring that the logic is simple and reusable.

## Managing Calculation History
The calculator stores a history of all performed operations, which can be accessed or cleared when needed. Users can:

- Retrieve the most recent calculation.
- Retrieve the entire history of calculations.
- Clear the history to reset the calculator’s state.
- These methods ensure that past operations are easily accessible while maintaining a clean and user-friendly experience.

## Testing the Project
This project includes extensive unit tests for each feature and operation. Testing is done using the pytest framework, and code linting is handled by pylint to ensure code quality.

To run the tests:

- Ensure that you have pytest installed in your environment.
- Run the tests using pytest. You can also include options to check for linting errors and code coverage.
The project has been fully tested, with 100% code coverage achieved through rigorous test cases.
