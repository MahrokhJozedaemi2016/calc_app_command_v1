"""
This module contains tests for the individual arithmetic operation functions: addition, subtraction, multiplication, and division.
It verifies the correctness of each operation with different input values.
"""
from decimal import Decimal
import pytest
from calculator.calculation import MathOperation  # Renamed Calculation to MathOperation
from calculator.operations import addition, subtraction, multiplication, division  #pylint: disable=unused-import

def test_operation(operand1, operand2, operation, expected):
    '''Testing various operations'''
    operation_instance = MathOperation.initialize(operand1, operand2, operation)  # Using initialize instead of create
    assert operation_instance.compute() == expected, f"{operation.__name__} operation failed"

# Keeping the divide by zero test as is since it tests a specific case
def test_divide_by_zero():
    '''Testing the divide by zero exception'''
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        operation_instance = MathOperation(Decimal('10'), Decimal('0'), division)
        operation_instance.compute()
