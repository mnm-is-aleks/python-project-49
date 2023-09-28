from brain_games.game_interfaces import get_interface
from brain_games.game_engine import game_loop
from brain_games.games.gcd import get_gcd


def main():
    name = get_interface('gcd')
    game_loop(name, get_gcd)


if __name__ == '__main__':
    main()
