from random import randint


def get_gcd(number_a, number_b):
    div_remainder = number_a % number_b
    while div_remainder != 0:
        number_a, number_b = number_b, div_remainder
        div_remainder = number_a % number_b
    return str(number_b)


def game_logic():
    number_a, number_b = randint(1, 10), randint(1, 10)
    question = f'{number_a} {number_b}'
    correct_answer = get_gcd(number_a, number_b)
    return question, correct_answer


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
