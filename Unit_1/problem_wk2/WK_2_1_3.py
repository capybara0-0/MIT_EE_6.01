"""
Problem Wk.2.1.3: Scoping
Enter the value of the expressions below. 
"""


def foo(x):
    def bar(x):
        return x + 1
    return bar(x * 2)


print(foo(3))
# The output is `7`


def foo_1(x):
    def bar(z):
        return x + z
    return bar(3)


print(foo_1(2))
# The output is `5`
