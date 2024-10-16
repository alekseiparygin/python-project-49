#! /usr/bin/env python3


from brain_games.scripts import engine
from brain_games.games import brain_calc_terms
from brain_games import cli

def main():
    engine.game_engine(brain_calc_terms.terms_of_brain_calc, 'What is the result of the expression?')


if __name__ == '__main__':
    main()
