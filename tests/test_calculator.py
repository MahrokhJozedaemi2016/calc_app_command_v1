import pytest
from calculator.calculator import Calculator
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

# Fixture to set up a calculator instance before each test
@pytest.fixture
def calc():
    return Calculator()

def test_add_command(calc):
    add_command = AddCommand(10, 5)
    result = calc.compute(add_command)
    assert result == 15, "Addition result is incorrect"

def test_subtract_command(calc):
    sub_command = SubtractCommand(10, 5)
    result = calc.compute(sub_command)
    assert result == 5, "Subtraction result is incorrect"

def test_multiply_command(calc):
    multiply_command = MultiplyCommand(10, 5)
    result = calc.compute(multiply_command)
    assert result == 50, "Multiplication result is incorrect"

def test_divide_command(calc):
    divide_command = DivideCommand(10, 5)
    result = calc.compute(divide_command)
    assert result == 2, "Division result is incorrect"

def test_divide_by_zero(calc):
    # Test divide by zero scenario
    divide_command = DivideCommand(10, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.compute(divide_command)
