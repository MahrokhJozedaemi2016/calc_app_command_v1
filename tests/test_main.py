from calculator import ArithmeticEngine
from calculator.calculations import OperationHistory
from decimal import Decimal, InvalidOperation

# Available commands
operation_mappings = {
    'add': ArithmeticEngine.add,
    'subtract': ArithmeticEngine.subtract,
    'multiply': ArithmeticEngine.multiply,
    'divide': ArithmeticEngine.divide
}

def display_menu():
    """Displays the list of available commands."""
    print("Available commands:")
    print("  add: Add two numbers")
    print("  subtract: Subtract two numbers")
    print("  multiply: Multiply two numbers")
    print("  divide: Divide two numbers")
    print("  history: View calculation history")
    print("  clear_history: Clear calculation history")
    print("  menu: Show available commands")
    print("  exit: Exit the calculator")

def calculate_and_store(a, b, operation_name):
    """Performs the calculation and stores it in history."""
    try:
        # Convert input to Decimal
        a_decimal, b_decimal = map(Decimal, [a, b])
        
        # Check if the operation exists in the mapping
        operation = operation_mappings.get(operation_name)
        
        if operation:
            # Perform the operation
            result = operation(a_decimal, b_decimal)
            print(f"The result of {operation_name} between {a} and {b} is {result}")
        else:
            print(f"Unknown operation: {operation_name}")
            return
        
        # Store the operation in history
        OperationHistory.record(result)
        
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def interactive_calculator():
    # Display welcome message
    print("Welcome to the interactive calculator!")
    print("Type 'menu' to see the available commands or 'exit' to quit.")
    print("Type 'history' to view past calculations or 'clear_history' to clear them.")
    
    while True:
        user_input = input("Enter a command (add, subtract, multiply, divide) followed by two numbers: ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        elif user_input.lower() == 'menu':
            display_menu()
        elif user_input.lower() == 'history':
            # View the history of calculations
            history = OperationHistory.retrieve_all()
            if history:
                for idx, operation in enumerate(history, 1):
                    print(f"{idx}: {operation}")
            else:
                print("No history available.")
        elif user_input.lower() == 'clear_history':
            # Clear the calculation history
            OperationHistory.clear_all()
            print("Calculation history cleared.")
        else:
            try:
                command, num1, num2 = user_input.split()
                # Perform and store the calculation
                calculate_and_store(num1, num2, command)
            except ValueError:
                print("Invalid input. Please provide a command followed by two numbers.")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    interactive_calculator()

