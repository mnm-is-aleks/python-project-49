#!/usr/bin/env python3
import brain_games.cli as cli


def greetings():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    return name


def main():
    greetings()


if __name__ == '__main__':
    main()
