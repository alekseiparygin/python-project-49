#! /usr/bin/env python3


from brain_games.scripts import engine
from brain_games.games import gcd


def main():
    engine.run_game(gcd.terms)


if __name__ == '__main__':
    main()
