"""
Problem Wk.3.1.3: Arithmetic if
Define a procedure arithmeticIf(v, a, b, c) that returns `a` if `v` is greater than 0, `b` if `v` is
equal to 0, and c if it is less than 0.
Your function should have type (num, *, *, *) -> *, where, by * we mean that it could be any type
"""


def arithmeticIf(v: float | int, a: any, b: any, c: any) -> any:
    if v > 0:
        return a
    elif v == 0:
        return b
    else:
        return c
