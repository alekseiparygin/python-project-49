#! /usr/bin/env python3


from brain_games.scripts import engine
from brain_games.games import calc


def main():
    engine.run_game(calc.terms, 'What is the result of the expression?')


if __name__ == '__main__':
    main()
