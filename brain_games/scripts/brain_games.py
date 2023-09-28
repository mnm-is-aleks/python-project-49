#!/usr/bin/env python3
import brain_games.cli as cli


name = None


def main():
    global name
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()


if __name__ == '__main__':
    main()
