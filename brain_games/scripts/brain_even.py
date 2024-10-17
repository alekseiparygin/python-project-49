#! /usr/bin/env python3


from brain_games.scripts import engine
from brain_games.games import brain_even_terms



def main():
    engine.game_engine(brain_even_terms.terms_of_brain_even, 'Answer "yes" if the number is even, otherwise answer "no".')



if __name__ == '__main__':
    main()