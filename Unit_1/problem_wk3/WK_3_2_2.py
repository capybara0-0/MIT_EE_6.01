"""
Problem Wk.3.2.2: Multiple times, again
Define a procedure multIAgen(m, n), which returns the product of m and n, both
arguments are integers, but can be positive or negative.
Don't use *, but assume that multIA from the last problem is already defined for you.
Your function should have type (int, int) -> int
"""

from WK_3_2_1 import multIA


def multi_agen(m: int, n: int) -> int:
    if n == 0 & m == 0:
        return 0
    if n > 0:
        return multIA(m, n)
    else:
        return -multIA(m, -n)


print(multi_agen(0, 5))
# 0
print(multi_agen(5, 0))
# 0
print(multi_agen(1, 5))
# 5
print(multi_agen(-1, 5))
# -5
print(multi_agen(-1, -5))
# 5
print(multi_agen(-5, -5))
# 25
print(multi_agen(-5, 5))
# -25
