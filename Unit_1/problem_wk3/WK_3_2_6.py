"""
Problem Wk.3.2.6: Powers of 2
Define a procedure p2(x) that takes an integer parameter x.
If x is greater than 1, the procedure returns the largest power of two that is less than x
otherwise, it returns 0.
Use a loop.
"""


def p2(x):
    if x <= 1:
        return 0
    power = 1
    while power * 2 < x:
        power *= 2
    return power
