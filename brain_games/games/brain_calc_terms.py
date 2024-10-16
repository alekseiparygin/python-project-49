import random


def terms_of_brain_calc():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    operator = random.choice(['+', '-', '*'])
    expression = f'{num1} {operator} {num2}'
    correct_answer = str(eval(expression))
    return expression, correct_answer