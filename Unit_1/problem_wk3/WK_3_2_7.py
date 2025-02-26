"""
Problem Wk.3.2.7: Perfectly square
Define a procedure perfectSquare(n), which returns True if n is a perfect square and
False otherwise. Your function should have type (positiveInt) -> boolean 
"""

import math


def perfect_square(n: int) -> bool:
    if n < 0:
        return False
    result = math.isqrt(n)
    return result * result == n


print(perfect_square(5))
print(perfect_square(26))
print(perfect_square(25))
print(perfect_square(36100))
