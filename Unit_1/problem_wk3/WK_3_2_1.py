"""
Problem Wk.3.2.1: Multiple times
Define a procedure multIA(m, n), which returns the product of `m` and `n`,
assuming that `n` is a positive integer.
Don't use * instead, use a while loop, and +.
Your function should have type(num, positiveInt) -> num
"""


def multIA(m: float | int, n: int) -> float | int:
    count = 0
    result = 0
    while count < n:
        result += m
        count += 1
    return result
