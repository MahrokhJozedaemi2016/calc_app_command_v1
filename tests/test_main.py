import pytest
from decimal import Decimal
from main import calculate_and_store, display_menu, prompt_for_numbers, interactive_calculator

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of add between 5 and 3 is 8"),
    ("10", "2", 'subtract', "The result of subtract between 10 and 2 is 8"),
    ("4", "5", 'multiply', "The result of multiply between 4 and 5 is 20"),
    ("20", "4", 'divide', "The result of divide between 20 and 4 is 5"),
    ("1", "1", 'divide', "The result of divide between 1 and 1 is 1"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero."),
    ("9", "3", 'unknown', "Unknown operation: unknown."),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")
])
def test_calculate_and_store(a_string, b_string, operation_string, expected_string, capsys):
    """Test the calculate_and_store function with various inputs."""
    calculate_and_store(a_string, b_string, operation_string)
    captured = capsys.readouterr().out.strip().rstrip(".")
    assert captured == expected_string.rstrip(".")

# Test for display_menu function
def test_display_menu(capsys):
    """Test that display_menu prints the correct menu options."""
    display_menu()
    captured = capsys.readouterr().out
    assert "Available commands:" in captured
    assert "add: Add two numbers" in captured
    assert "subtract: Subtract two numbers" in captured
    assert "multiply: Multiply two numbers" in captured
    assert "divide: Divide two numbers" in captured
    assert "history: View calculation history" in captured
    assert "clear_history: Clear calculation history" in captured
    assert "exit: Exit the calculator" in captured

# Test for prompt_for_numbers function
def test_prompt_for_numbers(monkeypatch):
    """Test prompt_for_numbers function with valid inputs."""
    inputs = iter(["10", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    a, b = prompt_for_numbers("add")
    assert a == "10"
    assert b == "5"

# Test for interactive_calculator function
def test_interactive_calculator(monkeypatch, capsys):
    """Test the interactive_calculator function with multiple commands."""
    inputs = iter(["menu", "add", "10", "20", "history", "clear_history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    interactive_calculator()

    captured = capsys.readouterr().out
    assert "Available commands:" in captured
    assert "The result of add between 10 and 20 is 30" in captured
    assert "Calculation history cleared." in captured
    assert "Goodbye!" in captured

# Additional test cases for invalid input handling
def test_calculate_and_store_invalid_input(capsys):
    """Test handling invalid input types in calculate_and_store."""
    calculate_and_store("foo", "bar", "add")
    captured = capsys.readouterr().out.strip()
    assert "Invalid number input: foo or bar is not a valid number." in captured

def test_calculate_and_store_zero_division(capsys):
    """Test handling division by zero in calculate_and_store."""
    calculate_and_store("10", "0", "divide")
    captured = capsys.readouterr().out.strip()
    assert "An error occurred: Cannot divide by zero." in captured

def test_unknown_command(capsys):
    """Test handling an unknown command in calculate_and_store."""
    calculate_and_store("10", "5", "modulus")
    captured = capsys.readouterr().out.strip()
    assert "Unknown operation: modulus" in captured
