from brain_games.games.even import is_even, task
from brain_games.game_engine import game_loop


def main():
    game_loop(is_even, task)


if __name__ == '__main__':
    main()
