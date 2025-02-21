"""
Part 1: Function Types
For each of the following functions, specify the type of the output. If it can be either an
int or a float, use num, which isn't a real Python type, but which we'll use to indicate that
either basic numeric type is legal.
In fact, in Python, booleans True and False can be operated on as if they were the
integers 1 and 0; but it is ugly and confusing to take advantage of this fact, and we will
resolutely pretend that it isn't true.
"""


def a(x):
    return x + 1
# The type of the output would be num | int | float


def b(x):
    return x + 1.0
# The type of the output would be num | float


def c(x, y):
    return x + y
# (Assuming that x and y are ints or floats.) Result: would be num | float


def d(x, y):
    return x > y
# The type of the output would be boolean


def e(x, y, z):
    return x >= y and x <= z
# The type of the output would be boolean


def f(x, y):
    return x + y - 2
# The type of the output would be num | float | int
