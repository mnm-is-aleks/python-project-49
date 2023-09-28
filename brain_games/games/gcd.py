from random import randint


def get_gcd():
    a, b = randint(1, 10), randint(1, 10)
    value = f'{a} {b}'
    n = a % b
    while n != 0:
        a, b = b, n
        n = a % b
    condition = b
    return value, condition
