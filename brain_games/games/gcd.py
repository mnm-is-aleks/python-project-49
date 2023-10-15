from random import randint


def game_logic():
    a, b = randint(1, 10), randint(1, 10)
    question = f'{a} {b}'
    n = a % b
    while n != 0:
        a, b = b, n
        n = a % b
    correct_answer = str(b)
    return question, correct_answer


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
