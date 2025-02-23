"""
Problem Wk.3.1.2: Compare
Define a procedure compare(x, y) that returns 1 if x is greater than y, 0 if x equals y and
-1 if x is less than y. Use elif to write the comparison.
"""


def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1
