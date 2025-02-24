"""
Problem Wk.3.1.5: Clip clop
Define a procedure clip(lo, x, hi) that returns `lo` if `x` is less than `lo`,
returns `hi` if `x` is greater than `hi`, and returns `x` otherwise.
You can assume that `lo < hi`.
This time, don't use 'if', but use 'min' and 'max'.
Your function should have type (num, num, num) -> num. 
"""


def clip(lo: float | int, x: float | int, hi: float | int) -> float | int:
    # ensure `x` does not exceed `hi`
    a = min(hi, x)

    # ensure the result is not less than `lo`
    return max(a, lo)

    # one liner
    # return max(lo, min(x, hi))
