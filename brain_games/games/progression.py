from random import randint
from random import choice


def make_progression():
    print('What number is missing in the progression?')
    n = int(choice('2345'))
    a = randint(1, 10)
    b = n * 10
    ls = [i for i in range(a, b + a, n)]
    current = randint(1, 8)
    correct_answer = str(ls[current])
    new_ls = [str(i) for i in ls]
    new_ls[current] = '..'
    question = " ".join(new_ls)
    return question, correct_answer
