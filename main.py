import sys
from calculator import ArithmeticEngine
from decimal import Decimal, InvalidOperation

def calculate_and_print(a, b, operation_name):
    # Map both old and new operation names
    operation_mappings = {
        'add': ArithmeticEngine.add,
        'addition': ArithmeticEngine.add,
        'subtract': ArithmeticEngine.subtract,
        'subtraction': ArithmeticEngine.subtract,
        'multiply': ArithmeticEngine.multiply,
        'multiplication': ArithmeticEngine.multiply,
        'divide': ArithmeticEngine.divide,
        'division': ArithmeticEngine.divide,
    }

    try:
        # Convert input to Decimal
        a_decimal, b_decimal = map(Decimal, [a, b])

        # Check if the operation exists in the mapping
        result = operation_mappings.get(operation_name)

        if result:
            # Perform the operation and print the result
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
        else:
            # Handle unknown operation
            print(f"Unknown operation: {operation_name}")
            sys.exit(1)

    # Handle division by zero first before generic exceptions
    except ZeroDivisionError:
        print("Error: Division by zero.")  # This should be triggered
        sys.exit(1)

    # Handle invalid decimal input
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
        sys.exit(1)

    # Handle unexpected exceptions
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    # Check that the user provided the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)

    # Unpack command-line arguments
    _, a, b, operation = sys.argv

    # Call the function to perform the operation
    calculate_and_print(a, b, operation)

if __name__ == '__main__':
    main()
