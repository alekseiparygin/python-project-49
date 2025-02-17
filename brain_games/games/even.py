import random


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_number(num):
    return num % 2 == 0


def game():
    num = random.randint(1, 100)
    expression = f'{num}'
    correct_answer = 'yes' if is_even_number(num) else 'no'
    return expression, correct_answer
