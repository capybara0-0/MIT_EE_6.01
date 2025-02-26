"""
Problem Wk.3.2.4: Muad-Div
Define a procedure div(m, n), which returns the integer part of m / n, where both
arguments are positive integers. Don't use /.
Your function should have type (positiveInt, positiveInt) -> positiveInt
"""


def div(m: int, n: int) -> int:
    quotient = 0
    while m >= n:
        m -= n
        quotient += 1
    return quotient
