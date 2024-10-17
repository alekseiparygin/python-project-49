#! /usr/bin/env python3


from brain_games.scripts import engine
from brain_games.games import brain_progression_terms


def main():
    engine.game_engine(brain_progression_terms.terms_of_brain_progression, 'What number is missing in this progression?')


if __name__ == '__main__':
    main()