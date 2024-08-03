"""
Math Functions in Python
========================

Python supports a variety of mathematical functions, ranging from basic arithmetic operations to advanced mathematical computations. The `math` and `numpy` libraries provide many built-in functions to perform these calculations efficiently.

Basic Arithmetic Operations:
-----------------------------
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Modulus (%)
- Exponentiation (**)
- Floor Division (//)

Examples:
"""
# Basic Arithmetic Operations
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)

"""
Math Module Functions:
----------------------
- The `math` module provides access to many mathematical functions and constants.

Examples:
"""
import math

# Constants
print("Pi:", math.pi)
print("Euler's Number:", math.e)
print("Tau:", math.tau)

# Trigonometric Functions
print("Sine of 90 degrees:", math.sin(math.radians(90)))
print("Cosine of 0 degrees:", math.cos(math.radians(0)))
print("Tangent of 45 degrees:", math.tan(math.radians(45)))

# Inverse Trigonometric Functions
print("Arcsine of 1:", math.degrees(math.asin(1)))
print("Arccosine of 0:", math.degrees(math.acos(0)))
print("Arctangent of 1:", math.degrees(math.atan(1)))

# Hyperbolic Functions
print("Hyperbolic sine of 1:", math.sinh(1))
print("Hyperbolic cosine of 1:", math.cosh(1))
print("Hyperbolic tangent of 1:", math.tanh(1))

# Exponential and Logarithmic Functions
print("Exponential of 2:", math.exp(2))
print("Natural logarithm of 2:", math.log(2))
print("Logarithm base 10 of 1000:", math.log10(1000))
print("Logarithm base 2 of 8:", math.log2(8))

# Power and Square Root Functions
print("Square root of 16:", math.sqrt(16))
print("3 raised to the power of 4:", math.pow(3, 4))

# Rounding Functions
print("Ceiling of 2.3:", math.ceil(2.3))
print("Floor of 2.7:", math.floor(2.7))
print("Absolute value of -5:", math.fabs(-5))

"""
NumPy Functions:
----------------
- NumPy is a library for numerical computations in Python. It provides support for arrays, matrices, and a large collection of mathematical functions.

Examples:
"""
import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Basic NumPy Functions
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Median:", np.median(arr))
print("Sum:", np.sum(arr))
print("Product:", np.prod(arr))

# Trigonometric Functions
print("Sine of array elements:", np.sin(arr))
print("Cosine of array elements:", np.cos(arr))
print("Tangent of array elements:", np.tan(arr))

# Exponential and Logarithmic Functions
print("Exponential of array elements:", np.exp(arr))
print("Natural logarithm of array elements:", np.log(arr))
print("Logarithm base 10 of array elements:", np.log10(arr))

# Power and Square Root Functions
print("Square root of array elements:", np.sqrt(arr))
print("Array elements raised to the power of 2:", np.power(arr, 2))

"""
Random Number Generation:
-------------------------
- The `random` module and `numpy.random` provide functions to generate random numbers and perform random operations.

Examples:
"""
import random

# Random number between 0 and 1
print("Random number between 0 and 1:", random.random())

# Random integer between 1 and 10
print("Random integer between 1 and 10:", random.randint(1, 10))

# Random choice from a list
choices = [1, 2, 3, 4, 5]
print("Random choice from list:", random.choice(choices))

# Shuffling a list
random.shuffle(choices)
print("Shuffled list:", choices)

# Using numpy.random
print("Random number from normal distribution:", np.random.normal())
print("Random integer between 1 and 10:", np.random.randint(1, 10))
print("Random choice from array:", np.random.choice(arr))
print("Random sample from array:", np.random.choice(arr, size=3, replace=False))
