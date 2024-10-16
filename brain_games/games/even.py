import random


def is_even_number(num):
    return 'yes' if num % 2 == 0 else 'no'


def terms():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'

    def game_logic():
        expression = random.randint(1, 100)
        s = is_even_number(expression)
        return expression, s

    return question, game_logic
