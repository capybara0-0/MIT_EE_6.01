"""
Problem Wk.2.2.6: Distance from point to line
Define a procedure perpDist(px, py, a, b, c) that returns the unsigned (positive)
distance between a point in two-dimensional space with coordinates px, py and a line
with equation ax + by + c == 0. Use math.sqrt (of type num -> float). Your function
should have type (num, num, num, num, num) -> float.
We don't necessarily expect you to remember or rederive this formula; try Google if
you need help.
You might find the function abs useful. 
"""
import math


def perp_dist(px: int | float, py: int | float, a: int | float, b: int | float, c: int | float) -> float:
    return abs(((a * px) + (b * py) + c) / math.sqrt(a * a + b * b))
