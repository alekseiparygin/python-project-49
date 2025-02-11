import random


def is_prime_number(num):
    if num < 2:
        return 'no'
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return 'no'
    return 'yes'


def prime():
    num = random.randint(1, 100)
    expression = f'{num}'
    s = is_prime_number(num)
    return expression, s
