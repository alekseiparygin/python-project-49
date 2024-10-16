import random
import prompt
from brain_games import cli

def checker(player_answer, correct_answer):
    if player_answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f"'{player_answer}' is a wrong answer ;(. Correct answer was '{correct_answer}'. Try again!")
        return False

def game_engine(game_name, welcome_message, check_func=checker):
    name = cli.welcome_user()
    print(welcome_message)
    num_of_rounds = 3
    for _ in range(num_of_rounds):
        expression, correct_answer = game_name()
        print(f'Question: {expression}')
        player_answer = prompt.string('Your answer: ').strip().lower()
        if not checker(player_answer, correct_answer):
            break
    else:
        print(f'Congratulations, {name}!')
