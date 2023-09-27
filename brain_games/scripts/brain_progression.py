from random import randint
from random import choice
from brain_games.scripts.game_interfaces import get_interface
from brain_games.scripts.game_engine import game_loop


def make_progression():
    n = int(choice('2345'))
    a = randint(1, 10)
    b = n * 10
    ls = [i for i in range(a, b+a, n)]
    current = randint(1, 8)
    condition = ls[current]
    new_ls = [str(i) for i in ls]
    new_ls[current] = '..'
    value = ", ".join(new_ls)
    return value, condition


def main():
    name = get_interface('progression')
    game_loop(name, make_progression)


if __name__ == '__main__':
    main()
