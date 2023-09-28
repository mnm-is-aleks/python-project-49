import prompt


def game_loop(name, game_logic):
    cnt = 0
    while cnt < 3:
        value, condition = game_logic()
        print(f'Question: {value}')
        if isinstance(condition, int):
            answer = prompt.integer('Your answer: ')
        elif isinstance(condition, str):
            answer = prompt.string('Your answer: ')
        else:
            break
        if condition == answer:
            cnt += 1
            print('Correct!')
        else:
            break
    if cnt == 3:
        print(f'Congratulations, {name}!')
    else:
        print(f"'{answer}' is wrong answer ;(."
              f"Correct answer was '{condition}'.\nLet's try again, {name}!")
