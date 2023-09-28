from brain_games.game_interfaces import get_interface
from brain_games.game_engine import game_loop
from brain_games.games.prime import is_prime


def main():
    name = get_interface('prime')
    game_loop(name, is_prime)


if __name__ == '__main__':
    main()
