from random import randint
from random import choice


def make_progression():
    n = int(choice('2345'))
    a = randint(1, 10)
    b = n * 10
    ls = [i for i in range(a, b + a, n)]
    current = randint(1, 8)
    condition = ls[current]
    new_ls = [str(i) for i in ls]
    new_ls[current] = '..'
    value = " ".join(new_ls)
    return value, condition
