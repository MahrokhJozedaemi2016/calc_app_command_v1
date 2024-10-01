"""
This module contains tests for the ArithmeticEngine class, which performs arithmetic operations
such as addition, subtraction, multiplication, and division.
"""
from calculator import ArithmeticEngine  # Renamed Calculator to ArithmeticEngine

def test_addition():
    '''Test that addition function works correctly'''    
    assert ArithmeticEngine.add(2, 2) == 4

def test_subtraction():
    '''Test that subtraction function works correctly'''    
    assert ArithmeticEngine.subtract(2, 2) == 0

def test_division():
    '''Test that division function works correctly'''    
    assert ArithmeticEngine.divide(2, 2) == 1

def test_multiplication():
    '''Test that multiplication function works correctly'''    
    assert ArithmeticEngine.multiply(2, 2) == 4
