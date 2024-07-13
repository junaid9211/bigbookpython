from datetime import datetime, timedelta
import random


def get_birthday():
    start_date = datetime(2000, 1, 1)
    birthday = start_date + timedelta(days=random.randint(0, 364))
    return birthday



def does_pair_exists(birthdays):
    for b in birthdays:
        if birthdays.count(b) > 1:
            return True

    return False

def get_pair_birthday(birthdays):
    for b in birthdays:
        if birthdays.count(b) > 1:
            return b



def get_birthday_str(birthday: datetime):
    months = {
        1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun',
        7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'
    }
    month_num = birthday.month
    month_name = months[month_num]
    birthday_str = f'{month_name} {birthday.day}'
    return birthday_str


def get_birthday_count():
    print("How many birthdays shall I generate? (Max 100)")
    while True:
        try:
            birthday_count = int(input("> "))
        except ValueError:
            print(f'You can only enter numbers')
        else:
            if birthday_count <= 100:
                return birthday_count
            else:
                print(f'Provided {birthday_count}, Please enter a value less than 100')


simulation_count = 100_000
birthday_count   = get_birthday_count()
birthdays = [get_birthday() for _ in range(birthday_count)]
birthday_strs = [get_birthday_str(b) for b in birthdays]
print(f'Here are {birthday_count} birthdays:')
print(f"{', '.join(birthday_strs)}")

pair_exists = does_pair_exists(birthdays)
if pair_exists:
    b = get_pair_birthday(birthdays)
    b_str = get_birthday_str(b)
    print(f"In this simulation, multiple people have a birthday on {b_str}")
else:
    print("In this simulation, there was no matching pair")


print(f"\nGenerating {birthday_count} random birthdays, {simulation_count} times...\n")
input("Press Enter to begin ")
print(f"Let's run another {simulation_count} simulations.")

count = 0
for i in range(simulation_count):
    if i % 10_000 == 0:
        print(f'{i} simulations run...')
    birthdays = [get_birthday() for _ in range(birthday_count)]
    pair_exists = does_pair_exists(birthdays)
    if pair_exists:
        count += 1

print(f'{simulation_count} simulations run...')
probablity = format(count/simulation_count * 100, '0.2f')

result = (f"Out of {simulation_count} simulations of {birthday_count} birthdays, there was a\n"
          f"matching birthday in that group {count} times. This means\n"
          f"that {birthday_count} people have a {probablity} % chance of\n"
          f"having a matching birthday in their group.\n"
          f"That's probably more than you would think!")


print(result)