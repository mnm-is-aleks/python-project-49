from brain_games.game_engine import game_loop
from brain_games.games.gcd import get_gcd, task


def main():
    game_loop(get_gcd, task)


if __name__ == '__main__':
    main()
