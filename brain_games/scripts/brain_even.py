from random import randint
from brain_games.scripts.game_interfaces import get_interface
from brain_games.scripts.game_engine import game_loop


def is_even():
    value = randint(1, 50)
    condition = value % 2 == 0 and 'yes' or 'no'
    return value, condition


def main():
    name = get_interface('even')
    game_loop(name, is_even)


if __name__ == '__main__':
    main()
