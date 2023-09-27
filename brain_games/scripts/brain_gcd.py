from random import randint
from brain_games.scripts.game_interfaces import get_interface
from brain_games.scripts.game_engine import game_loop


def get_gcd():
    a, b = randint(1, 10), randint(1, 10)
    value = f'{a} {b}'
    n = a % b
    while n != 0:
        a, b = b, n
        n = a % b
    condition = b
    return value, condition


def main():
    name = get_interface('gcd')
    game_loop(name, get_gcd)


if __name__ == '__main__':
    main()
