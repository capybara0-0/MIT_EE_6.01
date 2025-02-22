"""
Problem Wk.2.2.5: Evaluate a quadratic at a point
Define a procedure evalQuadratic(a, b, c, x) that returns the value of the quadratic ax2 + bx + c.
Your function should have type (num, num, num, num) -> num. 
"""


def eval_quadratic(a: int | float, b: int | float, c: int | float, x: int | float) -> int | float:
    return a * (x * x) + b * x + c
