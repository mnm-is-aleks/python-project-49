from brain_games.game_interfaces import get_interface
from brain_games.game_engine import game_loop
from brain_games.games.progression import make_progression


def main():
    name = get_interface('progression')
    game_loop(name, make_progression)


if __name__ == '__main__':
    main()
