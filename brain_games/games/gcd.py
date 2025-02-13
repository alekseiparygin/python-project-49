import random


QUESTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 + num2


def game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    expression = f'{num1} {num2}'
    correct_answer = str(find_gcd(num1, num2))
    return expression, correct_answer
