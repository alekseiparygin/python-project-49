import random


def calc():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    operator = random.choice(['+', '-', '*'])
    expression = f'{num1} {operator} {num2}'
    s = str(eval(expression))
    return expression, s
