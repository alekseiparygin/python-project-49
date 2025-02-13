import random


QUESTION = 'What number is missing in the progression?'


def make_list():
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    length = 10
    list = []
    for _ in range(length):
        list.append(start)
        start += step
    return list


def game():
    list = make_list()
    index = random.randint(0, len(list) - 1)
    random_element = list[index]
    list[index] = '..'
    expression = " ".join(map(str, list))
    correct_answer = str(random_element)
    return expression, correct_answer
