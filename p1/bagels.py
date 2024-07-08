"""
bagels practice
author: junaid mughal
"""
from utils import (
    gen_secret_num,
    get_input,
    did_win,
    get_hints
)

DIGITS = 3
GUESSES = 10

starting_message = (
    f'Bagels Program by Junaid9211\n'
    f'I will think of a secret number of {DIGITS} digits\n'
    f'You will have to guess it, you would have {GUESSES} tries'
)



def game_round():
    secret_num = gen_secret_num(DIGITS)
    print("I've thought of a secret number... ")
    # print(f'secret: {secret_num}')   For debug purpose
    cur_attempt = 1
    won = False
    while cur_attempt <= GUESSES:
        print(f'Guess #{cur_attempt}')
        user_input = get_input(DIGITS)

        cur_attempt += 1
        won = did_win(secret_num, user_input)
        if won:
            break

        hints = get_hints(secret_num, user_input)
        print(hints)

    if won:
        print("You won")
    else:
        print(f"You lost, the number was: {secret_num}")


def main():
    print(starting_message)
    playagain = True

    while playagain:
        game_round()
        playagain = input("Do you want to play again? (yes or no):  ") == "yes"

    print("Thanks for playing...")



if __name__ == '__main__':
    main()
