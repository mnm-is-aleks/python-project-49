from random import randint
from math import sqrt
from brain_games.scripts.game_interfaces import get_interface
from brain_games.scripts.game_engine import game_loop


def is_prime():
    n = randint(2, 30)
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return n, 'no'
    return n, 'yes'


def main():
    name = get_interface('prime')
    game_loop(name, is_prime)


if __name__ == '__main__':
    main()
