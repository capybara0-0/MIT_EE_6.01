"""
Problem Wk.3.2.5: Primo
Define a procedure prime(n), which returns True if n is prime and False otherwise.
It's okay if it's slow.
Your function should have type (positiveInt) -> boolean 
"""


def prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % i for i in range(3, int(n ** 0.5) + 1, 2))


print(prime(2))
print(prime(3))
print(prime(4))
print(prime(5))
print(prime(97))
print(prime(100))
print(prime(0))
