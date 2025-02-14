import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime_number(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def game():
    num = random.randint(1, 100)
    expression = f'{num}'
    correct_answer = 'yes' if is_prime_number(num) else 'no'
    return expression, correct_answer
