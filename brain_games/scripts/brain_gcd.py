#! /usr/bin/env python3


from brain_games.scripts import engine
from brain_games.games import brain_gcd_terms


def main():
    engine.game_engine(brain_gcd_terms.terms_of_brain_gcd, 'Find the greatest common divisor of given numbers.')


if __name__ == '__main__':
    main()