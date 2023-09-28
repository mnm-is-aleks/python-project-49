import brain_games.scripts.brain_games as bg


def get_interface(task):
    bg.main()
    name = bg.name
    match task:
        case 'calc':
            print('What is the result of the expression?')
        case 'even':
            print('Answer "yes" if the number is even, otherwise answer "no".')
        case 'gcd':
            print('Find the greatest common divisor of given numbers.')
        case 'progression':
            print('What number is missing in the progression?')
        case 'prime':
            print('Answer "yes" if given number is prime.'
                  ' Otherwise answer "no".')
    return name


def main():
    get_interface()


if __name__ == '__main__':
    main()