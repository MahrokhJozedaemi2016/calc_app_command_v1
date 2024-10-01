"""
This module provides basic arithmetic operations: addition, subtraction, multiplication, and division.
Each function accepts two Decimal operands and returns the result of the operation.
"""
from decimal import Decimal

# Define the arithmetic functions with updated names
def addition(x: Decimal, y: Decimal) -> Decimal:
    return x + y

def subtraction(x: Decimal, y: Decimal) -> Decimal:
    return x - y

def multiplication(x: Decimal, y: Decimal) -> Decimal:
    return x * y

def division(x: Decimal, y: Decimal) -> Decimal:
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

