from random import randint
from random import choice
import operator


def expression():
    op = choice('+-*')
    a, b = randint(1, 10), randint(1, 10)
    sl_op = {'+': operator.add, '*': operator.mul, '-': operator.sub}
    question = f'{a} {op} {b}'
    correct_answer = str(sl_op[op](a, b))
    return question, correct_answer


def task():
    print('What is the result of the expression?')
