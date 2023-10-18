from random import randint
from math import sqrt


def is_prime(rand_number):
    for i in range(2, int(sqrt(rand_number)) + 1):
        if rand_number % i == 0:
            return rand_number, 'no'
    return rand_number, 'yes'


def game_logic():
    rand_number = randint(2, 30)
    return is_prime(rand_number)


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
