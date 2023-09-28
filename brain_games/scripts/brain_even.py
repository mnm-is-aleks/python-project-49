from brain_games.games.even import is_even
from brain_games.game_interfaces import get_interface
from brain_games.game_engine import game_loop


def main():
    name = get_interface('even')
    game_loop(name, is_even)


if __name__ == '__main__':
    main()
