#!/usr/bin/env python
from random import randint
import prompt


def question():
    random_number = randint(1, 100)
    print(f'Question: {random_number}')
    print('Your answer:', end=' ')
    answer = input()
    a = random_number % 2 == 0 and answer == 'yes'
    b = random_number % 2 != 0 and answer == 'no'
    return ((a or b), answer, random_number)


def is_even():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    i = 1
    while i <= 3:
        argument = question()
        if argument[0] is False:
            if argument[2] % 2 == 0:
                right_answer = "\"yes\""
            else:
                right_answer = "\"no\""
            return print(f"""\"{argument[1]}\" is wrong answer ;(. \
Correct answer was {right_answer}.
Let\'s try again, {name}!""")
        print('Correct!')
        i = i + 1
    return print('Congratulations, ' + name + '!')


def main():
    is_even()


if __name__ == '__main__':
    main()
