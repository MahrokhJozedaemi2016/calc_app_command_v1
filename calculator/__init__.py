"""
This module initializes the calculator package and provides access to the key classes and operations
used for arithmetic calculations.
"""
# Import necessary modules and classes
from calculator.calculations import OperationHistory  # Updated to use OperationHistory
from calculator.operations import addition, subtraction, multiplication, division  # Updated function names
from calculator.calculation import MathOperation  # Updated to MathOperation (renamed from Calculation)
from decimal import Decimal  # For high-precision arithmetic
from typing import Callable  # For type hinting callable objects

# Definition of the ArithmeticEngine class (renamed Calculator)
class ArithmeticEngine:
    @staticmethod
    def _execute_operation(operand1: Decimal, operand2: Decimal, func: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Create and execute a calculation, then return the computed result."""
        # Generate a MathOperation object using the static create method with operands and the operation function
        operation_instance = MathOperation.initialize(operand1, operand2, func)
        # Add the calculation to the history managed by the OperationHistory class
        OperationHistory.record(operation_instance)
        # Execute the calculation and return the computed result
        return operation_instance.compute()

    @staticmethod
    def add(operand1: Decimal, operand2: Decimal) -> Decimal:
        # Perform addition by calling _execute_operation with the addition function
        return ArithmeticEngine._execute_operation(operand1, operand2, addition)

    @staticmethod
    def subtract(operand1: Decimal, operand2: Decimal) -> Decimal:
        # Perform subtraction by calling _execute_operation with the subtraction function
        return ArithmeticEngine._execute_operation(operand1, operand2, subtraction)

    @staticmethod
    def multiply(operand1: Decimal, operand2: Decimal) -> Decimal:
        # Perform multiplication by calling _execute_operation with the multiplication function
        return ArithmeticEngine._execute_operation(operand1, operand2, multiplication)

    @staticmethod
    def divide(operand1: Decimal, operand2: Decimal) -> Decimal:
        # Explicitly handle division by zero before performing the operation
        if operand2 == Decimal('0'):
            raise ZeroDivisionError("Cannot divide by zero")
        # Perform division by calling _execute_operation with the division function
        return ArithmeticEngine._execute_operation(operand1, operand2, division)
