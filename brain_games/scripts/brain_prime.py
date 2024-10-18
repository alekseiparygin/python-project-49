#! /usr/bin/env python3


from brain_games.scripts import engine
from brain_games.games import prime


def main():
    engine.run_game(prime.terms)


if __name__ == '__main__':
    main()
