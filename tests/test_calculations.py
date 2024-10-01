"""
This module contains tests for managing the history of arithmetic operations.
The tests verify the ability to add, retrieve, and clear calculation history.
"""

# Correct the import order by placing standard library imports before third-party library imports,
# adhering to PEP 8 guidelines for import ordering.
from decimal import Decimal
import pytest

# Import MathOperation and OperationHistory classes from the calculator package,
# assuming these are the correct paths following Python's package and module naming conventions.
from calculator.calculation import MathOperation  # Renamed from Calculation
from calculator.calculations import OperationHistory  # Renamed from Calculations

# Import arithmetic operation functions (addition and subtraction) to be tested.
from calculator.operations import addition, subtraction  # Renamed operations

# pytest.fixture is a decorator that marks a function as a fixture,
# a setup mechanism used by pytest to initialize a test environment.
# Here, it's used to define a fixture that prepares the test environment for operations tests.
@pytest.fixture
def setup_operations():
    """Clear history and add sample operations for tests."""
    # Clear any existing operation history to ensure a clean state for each test.
    OperationHistory.clear_all()
    # Add sample operations to the history to set up a known state for testing.
    # These operations represent typical use cases and allow tests to verify that
    # the history functionality is working as expected.
    OperationHistory.record(MathOperation(Decimal('10'), Decimal('5'), addition))
    OperationHistory.record(MathOperation(Decimal('20'), Decimal('3'), subtraction))

def test_record_operation(setup_operations):
    """Test adding an operation to the history."""
    # Create a new MathOperation object to add to the history.
    operation = MathOperation(Decimal('2'), Decimal('2'), addition)
    # Add the operation to the history.
    OperationHistory.record(operation)
    # Assert that the operation was added to the history by checking
    # if the latest operation in the history matches the one we added.
    assert OperationHistory.get_latest_record() == operation, "Failed to add the operation to the history"

def test_retrieve_all_operations(setup_operations):
    """Test retrieving the entire operation history."""
    # Retrieve the operation history.
    history = OperationHistory.retrieve_all()
    # Assert that the history contains exactly 2 operations,
    # which matches our setup in the setup_operations fixture.
    assert len(history) == 2, "History does not contain the expected number of operations"

def test_clear_all_operations(setup_operations):
    """Test clearing the entire operation history."""
    # Clear the operation history.
    OperationHistory.clear_all()
    # Assert that the history is empty by checking its length.
    assert len(OperationHistory.retrieve_all()) == 0, "History was not cleared"

def test_get_latest_record(setup_operations):
    """Test getting the latest operation from the history."""
    # Retrieve the latest operation from the history.
    latest = OperationHistory.get_latest_record()
    # Assert that the latest operation matches the expected values,
    # specifically the operands and operation used in the last added operation
    # in the setup_operations fixture.
    assert latest.operand1 == Decimal('20') and latest.operand2 == Decimal('3'), "Did not get the correct latest operation"

def test_find_by_operation_name(setup_operations):
    """Test finding operations in the history by operation type."""
    # Find all operations with the 'addition' operation.
    addition_operations = OperationHistory.find_by_operation_name("addition")
    # Assert that exactly one operation with the 'addition' operation was found.
    assert len(addition_operations) == 1, "Did not find the correct number of operations with addition operation"
    # Find all operations with the 'subtraction' operation.
    subtraction_operations = OperationHistory.find_by_operation_name("subtraction")
    # Assert that exactly one operation with the 'subtraction' operation was found.
    assert len(subtraction_operations) == 1, "Did not find the correct number of operations with subtraction operation"

def test_get_latest_record_with_empty_history():
    """Test getting the latest operation when the history is empty."""
    # Ensure the history is empty by clearing it.
    OperationHistory.clear_all()
    # Assert that the latest operation is None since the history is empty.
    assert OperationHistory.get_latest_record() is None, "Expected None for latest operation with empty history"
