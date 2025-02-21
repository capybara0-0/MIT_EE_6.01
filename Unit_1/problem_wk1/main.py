import math


print("<<============ WK.1.1.1 ============>>")
print(type(3.14).__name__)
print(type(-34))
print(type(True))
print(type(None))
print(type(3.0))


print("<<============ WK.1.1.2 ============>>")
print(6 + 12 - 3)
print(2.2 * 3.0)
print(- - 4)
print(10 / 3)
print(10.0 / 3.0)
print((2 + 3) * 4)
print(2 + 3 * 4)
print(2 ** 3 + 1)
print(2.1 ** 2.0)


print("<<============ WK.1.1.3 ============>>")
print("3 > 4: ", 3 > 4)
print("4.0 > 3.999 : ", 4.0 > 3.999)
print("4 > 4 : ", 4 > 4)
print("4 >= 4 : ", 4 >= 4)
print("2 + 2 == 4 : ", 2 + 2 == 4)
print("True or False : ", True or False)
print("False or False : ", False or False)
print("not False : ", not False)
print("3.0 - 1.0 != 5.0 - 3.0 : ", 3.0 - 1.0 != 5.0 - 3.0)
print("3 > 4 or (2 < 3 and 9 > 10) : ", 3 > 4 or (2 < 3 and 9 > 10))
print("4 > 5 or 3 < 4 and 9 > 8 : ", 4 > 5 or 3 < 4 and 9 > 8)
print("not (4 > 3 and 100 > 6) : ", not (4 > 3 and 100 > 6))


print("<<============ WK.1.1.4 ============>>")
# This time i want to try using a function to not repeat myself.


def mixed_type_expressions(expressions):
    for expression in expressions:
        result = eval(expression)
        print(f"{expression}: {result} type: {type(result).__name__}")


expressions = [
    "3 + 5.0",
    "5 / 2",
    "5/2 == 5/2.0",
    "5 / 2.0",
    "round(2.6)",
    "int(2.6)",
    "math.floor(2.6)",
    "2.0 + 5.0",
    "5 * 2 == 5.0 * 2.0"
]

mixed_type_expressions(expressions)
