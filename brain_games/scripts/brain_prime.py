import brain_games.scripts.brain_games as bg
from brain_games.game_engine import game_loop
from brain_games.games.prime import is_prime


def main():
    name = bg.greetings()
    game_loop(name, is_prime)


if __name__ == '__main__':
    main()
