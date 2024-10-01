"""
This module contains tests for the MathOperation class.
The tests validate the correct execution of arithmetic operations and proper representation of the operations.
"""

from decimal import Decimal
import pytest
from calculator.calculation import MathOperation  # Renamed Calculation to MathOperation
from calculator.operations import addition, subtraction, multiplication, division  # pylint: disable=unused-import

def test_math_operation_execution(operand1, operand2, operation, expected):
    """
    Test math operations with various scenarios.
    
    This test ensures that the MathOperation class correctly performs the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('operand1' and 'operand2'),
    and that the result matches the expected outcome.
    
    Parameters:
        operand1 (Decimal): The first operand in the calculation.
        operand2 (Decimal): The second operand in the calculation.
        operation (function): The arithmetic operation to perform.
        expected (Decimal): The expected result of the operation.
    """
    operation_instance = MathOperation(operand1, operand2, operation)  # Create a MathOperation instance with the provided operands and operation.
    assert operation_instance.compute() == expected, f"Failed {operation.__name__} operation with {operand1} and {operand2}"  # Perform the operation and assert that the result matches the expected value.

def test_math_operation_repr():
    """
    Test the string representation (__repr__) of the MathOperation class.
    
    This test verifies that the __repr__ method of a MathOperation instance returns a string
    that accurately represents the state of the MathOperation object, including its operands and operation.
    """
    operation_instance = MathOperation(Decimal('10'), Decimal('5'), addition)  # Create a MathOperation instance for testing.
    expected_repr = "MathOperation(10, 5, addition)"  # Define the expected string representation.
    assert repr(operation_instance) == expected_repr, "The __repr__ method output does not match the expected string."  # Assert that the actual string representation matches the expected string.

def test_division_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.
    
    This test checks that attempting to perform a division operation with a zero divisor
    correctly raises a ValueError, as dividing by zero is mathematically undefined and should be handled as an error.
    """
    operation_instance = MathOperation(Decimal('10'), Decimal('0'), division)  # Create a MathOperation instance with a zero divisor.
    with pytest.raises(ValueError, match="Cannot divide by zero"):  # Expect a ValueError to be raised.
        operation_instance.compute()  # Attempt to perform the calculation, which should trigger the ValueError.
