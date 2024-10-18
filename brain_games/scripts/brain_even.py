#! /usr/bin/env python3


from brain_games.scripts import engine
from brain_games.games import even


def main():
    engine.run_game(even.terms, 'Answer "yes" if the number is even, otherwise answer "no".')


if __name__ == '__main__':
    main()
