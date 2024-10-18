import random


def terms():
    question = 'What is the result of the expression?'

    def game_logic():
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        operator = random.choice(['+', '-', '*'])
        expression = f'{num1} {operator} {num2}'
        s = str(eval(expression))
        return expression, s

    return question, game_logic
