import prompt


def game_loop(name, game_logic):
    count = 0
    while count < 3:
        question, correct_answer = game_logic()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            count += 1
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f"Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break
        print(f'Congratulations, {name}!')
