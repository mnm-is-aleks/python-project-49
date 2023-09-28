from brain_games.game_interfaces import get_interface
from brain_games.game_engine import game_loop
from brain_games.games.calc import expression


def main():
    name = get_interface('calc')
    game_loop(name, expression)


if __name__ == '__main__':
    main()
