from brain_games.game_engine import game_loop
from brain_games.games.prime import is_prime, task


def main():
    game_loop(is_prime, task)


if __name__ == '__main__':
    main()
