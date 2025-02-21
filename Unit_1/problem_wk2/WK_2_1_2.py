"""
Problem Wk.2.1.2: Functions and Scope
Below is a transcript of a session with the Python shell. Provide the type and value of
the expressions being evaluated. If evaluating an expression would cause an error,
select noneType and write error in the box. If the value of an expression is a function,
select function as the type and write function in the box. 
"""

a = 10


def f(x):
    return x + a


a = 3
print(f(1))
print(type(f(1)).__name__)
# The type is `int` and the output is `4`

x = 12


def g(x):
    x = x + 1

    def h(y):
        return x + y
    return h(6)


print(g(x))
print(type(g(x)).__name__)
# The type is `int` and the output is `19`
