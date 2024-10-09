import random
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def is_even_number(num):
    if num % 2 == 0:
        return True
    else:
        return False


def brain_even():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        num = random.randint(1, 100)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if is_even_number(num):
            if answer == 'yes':
                print('Correct!')
                i += 1
                continue
            else:
                print("'{0}' is a wrong answer ;(. Correct answer was '{1}'. Let's try again, {2}!".format(answer, 'yes', name))
                break
            
        else:
            if answer == 'no':
                print('Correct!')
                i += 1
                continue
            else:
                print("'{0}' is a wrong answer ;(. Correct answer was '{1}'. Let's try again, {2}!".format(answer, 'no', name))
                break
   
    if i == 3:
        print(f'Congratulations, {name}!')