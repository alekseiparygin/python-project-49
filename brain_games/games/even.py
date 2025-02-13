import random


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_number(num):
    return 'yes' if num % 2 == 0 else 'no'


def game():
    expression = random.randint(1, 100)
    correct_answer = is_even_number(expression)
    return expression, correct_answer
