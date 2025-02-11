import prompt
from brain_games.cli import welcome_user


def run_game(game, question):
    name = welcome_user()
    print(question)
    num_of_rounds = 3
    for _ in range(num_of_rounds):
        expression, s = game()
        print(f'Question: {expression}')
        a = prompt.string('Your answer: ').strip().lower()
        if a != s:
            print(f"'{a}' is a wrong answer ;(. Correct answer was '{s}'.")
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {name}!')
