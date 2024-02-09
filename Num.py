import numpy as np

# Using numpy for arithmetic operations
def add(a, b):
    return np.add(a, b)

def subtract(a, b):
    return np.subtract(a, b)

def multiply(a, b):
    return np.multiply(a, b)

def divide(a, b):
    # Numpy's divide function automatically handles division by zero by returning inf or nan
    return np.divide(a, b)

# Example usage
a = 10
b = 5

add_result = add(a, b)
subtract_result = subtract(a, b)
multiply_result = multiply(a, b)
divide_result = divide(a, b)

print("Addition:", add_result)
print("Subtraction:", subtract_result)
print("Multiplication:", multiply_result)
print("Division:", divide_result)
