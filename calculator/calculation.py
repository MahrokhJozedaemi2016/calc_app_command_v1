"""
This module defines the MathOperation class which encapsulates an arithmetic operation.
The class supports operations such as addition, subtraction, multiplication, and division,
and provides methods to execute and represent the operation.
"""
# Import the Decimal class for precise decimal arithmetic
from decimal import Decimal
# Import Callable from typing to specify the operation as a callable type hint
from typing import Callable
# Import arithmetic operations from a module named calculator.operations
# Import the updated operations
from calculator.operations import addition, subtraction, multiplication, division

# Definition of the MathOperation class with type annotations for improved readability and safety (renamed Calculation)
class MathOperation:
    # Constructor method with type hints for parameters and the return type
    def __init__(self, operand1: Decimal, operand2: Decimal, operation_func: Callable[[Decimal, Decimal], Decimal]):
        # Initialize the first operand of the operation
        self.operand1 = operand1
        # Initialize the second operand of the operation
        self.operand2 = operand2
        # Store the operation as a callable that takes two Decimals and returns a Decimal
        self.operation_func = operation_func
    
    # Static method to create a new instance of MathOperation
    @staticmethod    
    def initialize(operand1: Decimal, operand2: Decimal, operation_func: Callable[[Decimal, Decimal], Decimal]):
        # Return a new MathOperation object initialized with the provided arguments
        return MathOperation(operand1, operand2, operation_func)

    # Method to execute the operation stored in this object
    def compute(self) -> Decimal:
        """Execute the stored operation and return the result."""
        return self.operation_func(self.operand1, self.operand2)

    # Special method to provide a string representation of the MathOperation instance
    def __repr__(self):
        """Return a simplified string representation of the operation."""
        return f"MathOperation({self.operand1}, {self.operand2}, {self.operation_func.__name__})"