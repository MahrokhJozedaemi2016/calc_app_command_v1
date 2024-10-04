from decimal import Decimal
from calculator.calculation import MathOperation
from calculator.calculations import OperationHistory
from calculator.operations import addition, subtraction, multiplication, division
from calculator import ArithmeticEngine

def main():
    print("Welcome to the interactive calculator! Type 'exit' to quit.")
    while True:
        user_input = input("Enter a command (add, subtract, multiply, divide) followed by two numbers: ").strip()

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            command, num1, num2 = user_input.split()
            num1, num2 = Decimal(num1), Decimal(num2)

            if command == 'add':
                result = ArithmeticEngine.add(num1, num2)
            elif command == 'subtract':
                result = ArithmeticEngine.subtract(num1, num2)
            elif command == 'multiply':
                result = ArithmeticEngine.multiply(num1, num2)
            elif command == 'divide':
                result = ArithmeticEngine.divide(num1, num2)
            else:
                print(f"Unknown command: {command}")
                continue

            print(f"Result: {result}")
        except ZeroDivisionError as e:
            print(e)
        except ValueError:
            print("Invalid input. Please provide a command followed by two numbers.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

