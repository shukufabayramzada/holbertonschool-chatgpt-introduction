#!/usr/bin/python3

import sys

def factorial(n):
    """
    Calculates the factorial of a non-negative integer.

    Parameters:
    n (int): The non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the input integer
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

if len(sys.argv) != 2:
    print("Usage: python3 factorial_recursive.py <number>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
except ValueError:
    print("Error: Please provide an integer.")
    sys.exit(1)

if num < 0:
    print("Error: Factorial is not defined for negative numbers.")
    sys.exit(1)

f = factorial(num)
print(f)

