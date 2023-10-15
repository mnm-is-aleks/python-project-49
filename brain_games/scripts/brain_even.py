from brain_games.games.even import is_even
import brain_games.scripts.brain_games as bg
from brain_games.game_engine import game_loop


def main():
    name = bg.greetings()
    game_loop(name, is_even)


if __name__ == '__main__':
    main()
