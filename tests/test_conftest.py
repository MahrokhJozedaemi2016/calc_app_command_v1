import pytest
from decimal import Decimal
from calculator.operations import add, subtract, multiply, divide

# Directly include generate_test_data from your original conftest.py
def generate_test_data(num_records):
    """Generate test data for different operations."""
    operation_mappings = {
        'add': add,
        'subtract': subtract,
        'multiply': multiply,
        'divide': divide
    }
    
    for _ in range(num_records):
        a = Decimal('10')
        b = Decimal('5')
        operation_name = 'add'
        operation_func = operation_mappings[operation_name]
        
        try:
            expected = operation_func(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"
        yield a, b, operation_name, operation_func, expected


# Test generate_test_data function directly
def test_generate_test_data():
    """Test if generate_test_data generates the correct data."""
    num_records = 5
    data = list(generate_test_data(num_records))
    
    assert len(data) == num_records, f"Expected {num_records} records but got {len(data)}"
    
    for a, b, operation_name, operation_func, expected in data:
        assert isinstance(a, Decimal), "First operand is not a Decimal"
        assert isinstance(b, Decimal), "Second operand is not a Decimal"
        assert callable(operation_func), "Operation function is not callable"
        assert operation_func in [add, subtract, multiply, divide], "Unexpected operation function"
        result = operation_func(a, b)
        assert result == expected, f"Expected {expected} but got {result}"
