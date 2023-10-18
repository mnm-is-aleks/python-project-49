from random import randint


def is_even(number):
    return number % 2 == 0


def game_logic():
    number = randint(1, 50)
    correct_answer = is_even(number) and 'yes' or 'no'
    return number, correct_answer


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
