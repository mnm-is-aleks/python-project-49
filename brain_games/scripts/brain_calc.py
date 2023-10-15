from brain_games.game_engine import game_loop
from brain_games.games.calc import expression, task


def main():
    game_loop(expression, task)


if __name__ == '__main__':
    main()
