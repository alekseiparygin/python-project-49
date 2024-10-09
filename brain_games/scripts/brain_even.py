#! /usr/bin/env python3


from brain_games import even_numbers


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    even_numbers.brain_even()


if __name__ == '__main__':
    main()