from random import randint


def game_logic():
    question = randint(1, 50)
    correct_answer = question % 2 == 0 and 'yes' or 'no'
    return question, correct_answer


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
