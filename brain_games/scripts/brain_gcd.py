import brain_games.scripts.brain_games as bg
from brain_games.game_engine import game_loop
from brain_games.games.gcd import get_gcd


def main():
    name = bg.greetings()
    game_loop(name, get_gcd)


if __name__ == '__main__':
    main()
