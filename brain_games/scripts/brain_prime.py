#! /usr/bin/env python3


from brain_games.scripts import engine
from brain_games.games import brain_prime_terms


def main():
    engine.game_engine(brain_prime_terms.terms_of_brain_prime, 'Answer "yes" if given number is prime, otherwise answer "no".')



if __name__ == '__main__':
    main()