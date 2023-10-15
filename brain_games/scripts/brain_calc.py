import brain_games.scripts.brain_games as bg
from brain_games.game_engine import game_loop
from brain_games.games.calc import expression


def main():
    name = bg.greetings()
    game_loop(name, expression)


if __name__ == '__main__':
    main()
