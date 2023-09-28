from random import randint
from random import choice
import operator
from brain_games.scripts.game_interfaces import get_interface
from brain_games.scripts.game_engine import game_loop


def expression():
    op = choice('+-*')
    a, b = randint(1, 10), randint(1, 10)
    sl_op = {'+': operator.add, '*': operator.mul, '-': operator.sub}
    value = f'{a} {op} {b}'
    condition = sl_op[op](a, b)
    return value, condition


def main():
    name = get_interface('calc')
    game_loop(name, expression)


if __name__ == '__main__':
    main()
