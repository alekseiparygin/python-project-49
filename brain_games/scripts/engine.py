import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def checker(answer, solution):
    if answer == solution:
        print('Correct!')
        return True
    else:
        return False


def run_game(game_terms, check_func=checker):
    name = welcome_user()
    question, game_logic = game_terms()
    print(question)
    num_of_rounds = 3
    for _ in range(num_of_rounds):
        expression, solution = game_logic()
        print(f'Question: {expression}')
        answer = prompt.string('Your answer: ').strip().lower()
        if not checker(answer, solution):
            print(f"'{answer}' is a wrong answer ;(. Correct answer was '{solution}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
