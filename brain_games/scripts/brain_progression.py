#! /usr/bin/env python3


from brain_games.scripts import engine
from brain_games.games import progression


def main():
    engine.run_game(progression.terms)


if __name__ == '__main__':
    main()
