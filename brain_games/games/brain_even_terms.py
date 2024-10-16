import random

def is_even_number(num):
    return 'yes' if num % 2 == 0 else 'no'


def terms_of_brain_even():
    expression = random.randint(1, 100)
    correct_answer = is_even_number(expression)
    return expression, correct_answer