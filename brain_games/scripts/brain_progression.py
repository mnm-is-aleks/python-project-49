from brain_games.game_engine import game_loop
from brain_games.games.progression import make_progression, task


def main():
    game_loop(make_progression, task)


if __name__ == '__main__':
    main()
