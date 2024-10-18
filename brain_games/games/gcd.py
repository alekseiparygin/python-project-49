import random


def find_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def terms():
    question = 'Find the greatest common divisor of given numbers.'

    def game_logic():
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        expression = f'{num1} {num2}'
        solution = str(find_gcd(num1, num2))
        return expression, solution

    return question, game_logic
