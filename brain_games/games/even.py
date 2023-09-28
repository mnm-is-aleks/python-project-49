from random import randint


def is_even():
    value = randint(1, 50)
    condition = value % 2 == 0 and 'yes' or 'no'
    return value, condition
