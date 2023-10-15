import brain_games.scripts.brain_games as bg
from brain_games.game_engine import game_loop
from brain_games.games.progression import make_progression


def main():
    name = bg.greetings()
    game_loop(name, make_progression)


if __name__ == '__main__':
    main()
