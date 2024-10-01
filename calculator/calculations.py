"""
This module manages the history of calculations performed by the MathOperation class.
It provides methods for adding new calculations, retrieving the history, and clearing the history.
"""
from decimal import Decimal
from typing import Callable, List

from calculator.calculation import MathOperation  # Renamed Calculation to MathOperation

class OperationHistory:
    # Renamed the class from Calculations to OperationHistory
    records: List[MathOperation] = []

    @classmethod
    def record(cls, operation: MathOperation):
        """Record a new operation in the history."""
        cls.records.append(operation)

    @classmethod
    def retrieve_all(cls) -> List[MathOperation]:
        """Retrieve the complete operation history."""
        return cls.records

    @classmethod
    def clear_all(cls):
        """Clear the entire operation history."""
        cls.records.clear()

    @classmethod
    def get_latest_record(cls) -> MathOperation:
        """Get the most recent operation. Returns None if no history is available."""
        if cls.records:
            return cls.records[-1]
        return None

    @classmethod
    def find_by_operation_name(cls, operation_name: str) -> List[MathOperation]:
        """Find and return a list of operations by their operation name."""
        return [op for op in cls.records if op.operation_func.__name__ == operation_name]