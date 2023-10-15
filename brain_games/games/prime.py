from random import randint
from math import sqrt


def is_prime():
    print('Answer "yes" if given number is prime.'
          ' Otherwise answer "no".')
    n = randint(2, 30)
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return n, 'no'
    return n, 'yes'
