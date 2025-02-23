# Problem Wk.3.1.1: If statements
"""
Below is a transcript of a session with the Python shell. Provide the type and value of
the expressions being evaluated. If evaluating an expression would cause an error,
select noneType and write error in the box. If the result is a function, select function
and write function in the box. Assume the following definitions have been made:
"""


def a(x, y, z):
    if x:
        return y
    else:
        return z


def b(y, z):
    return a(y > z, y, z)


print(a(False, 2, 3))
# 1. The output is `3` and the type is `int`.


print(b(3, 2))
# 2. The output is `3` and the type is `int`.

print(a(3 > 2, a, b))
# 3. The output is `function refernce to a` and the type is `function`

print(b(a, b))
# 4. The output is `TypeError` and the type is `noneType`
