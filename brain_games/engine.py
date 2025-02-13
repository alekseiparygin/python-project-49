import prompt
from brain_games.cli import welcome_user


MAX_ROUNDS = 3


def run_game(game):
    name = welcome_user()
    question = game.QUESTION
    print(question)
    for _ in range(MAX_ROUNDS):
        expression, correct_answer = game.game()
        print(f'Question: {expression}')
        answer = prompt.string('Your answer: ').strip().lower()
        if answer != correct_answer:
            print(
                f"'{answer}' is a wrong answer ;(. Correct answer was '{correct_answer}'."
                )
            print(f"Let's try again, {name}!")
            return
        else:
            print('Correct!')
    
        print(f'Congratulations, {name}!')
