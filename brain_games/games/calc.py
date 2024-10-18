import random


def terms():
    question = 'What is the result of the expression?'

    def game_logic():
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        operator = random.choice(['+', '-', '*'])
        expression = f'{num1} {operator} {num2}'
        solution = str(eval(expression))
        return expression, solution
    
    return question, game_logic
