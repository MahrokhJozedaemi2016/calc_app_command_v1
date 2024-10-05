import pytest
from calculator.plugins.divide_plugin import DivideCommand, register

def test_divide_command():
    """Test normal division in DivideCommand"""
    divide_command = DivideCommand(10, 2)
    result = divide_command.execute()
    assert result == 5, "Division result is incorrect"

def test_divide_command_by_zero():
    """Test division by zero in DivideCommand"""
    divide_command = DivideCommand(10, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide_command.execute()

# New test to cover the register() function (Line 14)
def test_register_divide_command():
    """Test the register function to ensure it returns the correct class."""
    command_class = register()  # Call the register function
    assert command_class == DivideCommand, "register() did not return the expected DivideCommand class"
