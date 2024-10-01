"""
This module provides pytest fixtures and test data generation for arithmetic operations
used in the calculator application.
"""
import sys
import pytest
from main import calculate_and_print, main


@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'addition', "The result of 5 addition 3 is equal to 8"),
    ("10", "2", 'subtraction', "The result of 10 subtraction 2 is equal to 8"),
    ("4", "5", 'multiplication', "The result of 4 multiplication 5 is equal to 20"),
    ("20", "4", 'division', "The result of 20 division 4 is equal to 5"),
])
def test_calculate_and_print_valid_cases(a_string, b_string, operation_string, expected_string, capsys):
    """
    Test the calculate_and_print function with valid inputs and operations.
    These cases should not raise SystemExit.
    """
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string


@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("1", "0", 'division', "Error: Division by zero."),
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    ("a", "3", 'addition', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtraction', "Invalid number input: 5 or b is not a valid number.")
])
def test_calculate_and_print_error_cases(a_string, b_string, operation_string, expected_string, capsys):
    """
    Test the calculate_and_print function with error scenarios, which should raise SystemExit.
    """
    with pytest.raises(SystemExit):
        calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert expected_string in captured.out.strip()


def test_generic_exception(monkeypatch, capsys):
    """
    Test that a generic exception is caught and handled.
    """
    def mock_decimal(value):
        raise ValueError("Unexpected error")  # Use a more specific exception type

    # Apply the monkeypatch to mock Decimal
    monkeypatch.setattr("main.Decimal", mock_decimal)

    # Run the calculate_and_print function which should trigger the mocked exception
    with pytest.raises(SystemExit):  # Expect SystemExit due to sys.exit(1)
        calculate_and_print("10", "5", "addition")
    captured = capsys.readouterr()
    assert "An unexpected error occurred: Unexpected error" in captured.out.strip()


def test_divide_by_zero_in_main(monkeypatch, capsys):
    """
    Test division by zero using main function.
    """
    # Simulate passing "1", "0", "division" to trigger the ZeroDivisionError
    monkeypatch.setattr(sys, 'argv', ['main.py', '1', '0', 'division'])
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "Error: Division by zero." in captured.out.strip()


def test_main_invalid_arguments(monkeypatch, capsys):
    """
    Test that the main function exits when the number of arguments is invalid.
    """
    monkeypatch.setattr(sys, 'argv', ['main.py', '1', 'add'])  # Invalid number of arguments
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert "Usage: python main.py <number1> <number2> <operation>" in captured.out.strip()
