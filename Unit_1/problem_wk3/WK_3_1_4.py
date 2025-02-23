"""
Problem Wk.3.1.4: Clipping shears
Define a procedure clip(lo, x, hi) that returns `lo` if `x` is less than `lo`, returns `hi` if `x` is
greater than `hi`, and returns `x` otherwise.
Use "if." Your function should have type (num, num, num) -> num. 
"""


def clip(lo: float | int, x: float | int, hi: float | int) -> float | int:
    if x < lo:
        return lo
    elif x > hi:
        return hi
    else:
        return x
