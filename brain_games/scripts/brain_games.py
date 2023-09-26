#!/usr/bin/env python3
import brain_games.cli as cli


def main():
    print('Welcome to the Brain Games!')
    name = cli.welcome_user()
    return name


if __name__ == '__main__':
    main()
