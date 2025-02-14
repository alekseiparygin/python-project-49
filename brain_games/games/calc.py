import random


QUESTION = 'What is the result of the expression?'


def game():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    operator = random.choice(['+', '-', '*'])
    
    match operator:
        case '+':
            correct_answer = str(num1 + num2)
        case '-':
            correct_answer = str(num1 - num2)
        case '*':
            correct_answer = str(num1 * num2)
            
    expression = f'{num1} {operator} {num2}'
    return expression, correct_answer
