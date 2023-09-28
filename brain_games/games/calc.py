from random import randint
from random import choice
import operator


def expression():
    op = choice('+-*')
    a, b = randint(1, 10), randint(1, 10)
    sl_op = {'+': operator.add, '*': operator.mul, '-': operator.sub}
    value = f'{a} {op} {b}'
    condition = sl_op[op](a, b)
    return value, condition
