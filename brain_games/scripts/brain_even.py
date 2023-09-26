from random import randint
import prompt
import brain_games.scripts.brain_games as mn


def is_even(n):
    return n % 2 == 0


def game_even():
    name = mn.main()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    cnt = 0
    while cnt < 3:
        n = randint(1, 50)
        print(f'Question: {n}')
        answer = prompt.string('Your answer: ')
        if answer not in ('yes', 'no'):
            break
        else:
            if (is_even(n) and 'yes' or 'no') == answer:
                cnt += 1
                print('Correct!')
            else:
                break
    if cnt == 3:
        print(f'Congratulations, {name}!')


def main():
    game_even()


if __name__ == '__main__':
    main()
