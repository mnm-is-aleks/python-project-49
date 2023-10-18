from random import randint
from random import choice
import operator


def calculate(current_operator, number_a, number_b):
    correct_answer = str(current_operator(number_a, number_b))
    return correct_answer


def game_logic():
    rand_operator = choice('+-*')
    number_a, number_b = randint(1, 10), randint(1, 10)
    dct_operator = {'+': operator.add, '*': operator.mul, '-': operator.sub}
    current_operator = dct_operator[rand_operator]
    question = f'{number_a} {rand_operator} {number_b}'
    correct_answer = calculate(current_operator, number_a, number_b)
    return question, correct_answer


DESCRIPTION = 'What is the result of the expression?'
