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


"""
Part 2: Transcript
Below is a transcript of a session with the Python shell. Assume the functions from part
1 have been defined. Provide the type and value of the expressions being evaluated. If
evaluating an expression would cause an error, select noneType and write error in the
box. If the value of an expression is a function, select function as the type and write
function in the box. 
"""

a(6)
# The output is `7` and it's type is `int || num`

a(-5.3)
# The output is `-4.3` and it's type is `float || num`

a(a(a(6)))
# The output is `9` and it's type is `int || num`

c(a(1), b(1))
# The output is `4.0` and it's type is `float || num`

d(10, 11.1)
# The output is `False` and it's type is `boolean`

e(a(3), b(4), c(3, 4))
# The output is `False` and it's type is `boolean`

e
# Type function
