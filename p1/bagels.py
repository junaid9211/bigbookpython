"""
bagels practice
author: junaid mughal
"""

import random

digits = 3
guesses = 10

starting_message = ('Bagels Program...'
                    f'I have a secret number, of {digits} can you guess what it is? You have {guesses} tries')


def gen_secret_num(digit_count: int) -> str:
    digits = list('0123456789')
    random.shuffle(digits)
    secret_num = ''.join(digits[i] for i in range(digit_count))
    return secret_num


def get_input(digit_count):
    while True:
        user_input = input("> ").strip()
        if user_input.isdigit() and len(user_input) == digit_count:
            return user_input
        else:
            print(f'Incorrect format. provide 3 digits, ex 123')


def compare(secret, user_input):
    hints = []
    if user_input == secret:
        print(f'You won')
        return True

    for i, c in enumerate(user_input):
        if c in secret:
            if c == secret[i]:
                hints.append("Fermi")
            else:
                hints.append("Pico")

    if not hints:
        hints.append("Bagel")

    hints.sort()
    print(' '.join(hints))
    return False


def main():
    print(starting_message)
    playagain = True

    while playagain:
        secret_num = gen_secret_num(digits)
        print("I've thought of a secret number... ")
        # print(f'secret: {secret_num}')   For debug purpose
        cur_attempt = 1
        won = False
        while cur_attempt <= guesses:
            print(f'Guess #{cur_attempt}')
            user_input = get_input(digits)
            cur_attempt += 1
            won = compare(secret_num, user_input)
            if won:
                break

        if not won:
            print(f"You lost, the number was: {secret_num}")
        playagain = input("Do you want to play again? (yes or no):  ") == "yes"

    print("Thanks for playing...")


if __name__ == '__main__':
    main()
