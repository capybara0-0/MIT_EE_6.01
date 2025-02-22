"""
Problem Wk.2.2.2: Fourth Power
Define a procedure fourthPower(x) that takes a numeric parameter x and returns that
value raised to the fourth power. It should have type num -> num. You should use the
square procedure (you don't need to redefine it in this box; it will use our definition
when your code is run by the tutor). 
"""

from WK_2_2_1 import square


def fourth_power(x: int | float) -> int | float:
    return square(square(x))
