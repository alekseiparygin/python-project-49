import random


QUESTION = 'What is the result of the expression?'


def game():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    operator = random.choice(['+', '-', '*'])
    expression = f'{num1} {operator} {num2}'
    correct_answer = str(eval(expression))
    return expression, correct_answer
