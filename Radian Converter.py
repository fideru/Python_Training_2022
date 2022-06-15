# Radians function
# 2022 - 06 - 03
import math


def degree_converter():
    degrees = input('Enter the degree to convert to radians: ')
    radians = int(degrees) * (math.pi / 180)
    return radians


def fibonacci(n):
    error_code = 'Error: n must be an  positive integer'
    if type(n) != int:
        return (error_code)
    elif n < 0:
        return (error_code)
    if n == 0:
        return 1
    elif n == 1 or n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Change the following n to the number you desire to evaluate.
print(fibonacci(50))
