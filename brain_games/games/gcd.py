import random


def find_gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def gcd():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    expression = f'{num1} {num2}'
    s = str(find_gcd(num1, num2))
    return expression, s
