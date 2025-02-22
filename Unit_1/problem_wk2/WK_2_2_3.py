"""
Problem Wk.2.2.3: Odd Test
Define a procedure odd(x) that returns True when its integer argument is an odd
number and False otherwise. It should have type int -> boolean. Use the % (mod)
operator, not if .
"""


def odd(x: int) -> bool:
    return x % 2 == 1


print(odd(100))
print(odd(99))
