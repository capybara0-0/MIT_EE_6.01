"""
Problem Wk.3.2.3: A la mod
Define a procedure mod(m, n), which returns m mod n, where both arguments are
positive integers.Don't use %.
Your function should have type (positiveInt, positiveInt) -> positiveInt 
"""


def mod(m: int, n: int) -> int:
    while m >= n:
        m -= n
    return m


print(mod(5, 2))


def mod_without_loop(m: int, n: int) -> int:
    return m - (m // n) * n


print(mod_without_loop(10, 3))
