import random


def is_even_number(num):
    return 'yes' if num % 2 == 0 else 'no'


def even():
    expression = random.randint(1, 100)
    s = is_even_number(expression)
    return expression, s
