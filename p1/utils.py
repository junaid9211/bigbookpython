import random


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


def did_win(secret, user_input):
    return secret == user_input



def get_hints(secret, user_input):
    hints = []
    for i, c in enumerate(user_input):
        if c in secret:
            if c == secret[i]:
                hints.append("Fermi")
            else:
                hints.append("Pico")

    if not hints:
        hints.append("Bagel")

    hints.sort()
    return ' '.join(hints)

