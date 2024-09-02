#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number recursively.

    Parameters:
    n (int): The number for which to calculate the factorial. 
             Must be a non-negative integer.

    Returns:
    int: The factorial of the given number. 
         If n is 0, returns 1 (since 0! is defined as 1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get the number from command line arguments, calculate the factorial, and print the result
f = factorial(int(sys.argv[1]))
print(f)
