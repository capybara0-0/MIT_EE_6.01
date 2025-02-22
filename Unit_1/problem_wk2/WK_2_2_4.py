"""
Problem Wk.2.2.4: From point A to point B
Define a procedure pointDist(x1, y1, x2, y2) that returns the distance between a point
in two-dimensional space with coordinates x1, y1 and another point with coordinates x2, y2.
Use math.sqrt (of type num -> float). 
Your function should have type (num, num, num, num) -> float. 
"""

import math
from WK_2_2_1 import square


def pointDist(x1: int | float, y1: int | float, x2: int | float, y2: int | float) -> float:
    return math.sqrt(square((x2 - x1)) + square((y2 - y1)))
