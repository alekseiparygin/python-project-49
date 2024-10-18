import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def checker(player_answer, correct_answer):
    if player_answer == correct_answer:
        print('Correct!')
        return True
    else:
        return False


def run_game(game_name, welcome_message, check_func=checker):
    name = welcome_user()
    print(welcome_message)
    num_of_rounds = 3
    for _ in range(num_of_rounds):
        expression, correct_answer = game_name()
        print(f'Question: {expression}')
        player_answer = prompt.string('Your answer: ').strip().lower()
        if not checker(player_answer, correct_answer):
            print(f"'{player_answer}' is a wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')
