import prompt
from brain_games.cli import welcome_user


MAX_ROUNDS = 3
WRONG_ANSWER_MSG = """'{}' is a wrong answer ;(. Correct answer was '{}'.
Let's try again, {}!"""


def run_game(game):
    name = welcome_user()
    question = game.QUESTION
    print(question)
    for _ in range(MAX_ROUNDS):
        expression, correct_answer = game.game()
        print(f'Question: {expression}')
        answer = prompt.string('Your answer: ').strip().lower()
        if answer != correct_answer:
            print(WRONG_ANSWER_MSG.format(answer, correct_answer, name))
            return
        else:
            print('Correct!')
            
    print(f'Congratulations, {name}!')
