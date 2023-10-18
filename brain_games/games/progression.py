from random import randint
from random import choice


def get_progression(start_num, finish_num, step):
    progression = [i for i in range(start_num, finish_num + start_num, step)]
    current_position = randint(1, 8)
    correct_answer = str(progression[current_position])
    return progression, current_position, correct_answer


def game_logic():
    step = int(choice('2345'))
    start_num = randint(1, 10)
    finish_num = step * 10
    progression, current_position, correct_answer = (
        get_progression(start_num, finish_num, step)
    )
    progression_str = [str(i) for i in progression]
    progression_str[current_position] = '..'
    question = " ".join(progression_str)
    return question, correct_answer


DESCRIPTION = 'What number is missing in the progression?'
