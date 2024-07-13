import random
from dataclasses import dataclass, field

# Set up the constants:
HEARTS   = chr(9829)  # Character 9829 is '♥'.
DIAMONDS = chr(9830)  # Character 9830 is '♦'.
SPADES   = chr(9824)  # Character 9824 is '♠'.
CLUBS    = chr(9827)  # Character 9827 is '♣'.
BACKSIDE = 'backside'
INITIAL_DEPOSIT = 5000



def generate_deck():
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = [HEARTS, DIAMONDS, SPADES, CLUBS]
    deck = [Card(r, s) for r in ranks for s in suits]
    random.shuffle(deck)
    return deck



# generate cards
@dataclass
class Card:
    rank: str
    suit: str


@dataclass
class Deck:
    cards: list[Card] = field(default_factory=generate_deck)

    def get_card(self):
        card = self.cards.pop()
        return card


def display_cards(cards: list[Card]):
    rows = ['', '', '', '', '']
    for c in cards:
        rows[0] += " ___  "
        if c == BACKSIDE:
            rows[1] += f"|## | "
            rows[2] += f"|###| "
            rows[3] += f"|_##| "

        else:
            rows[1] += f"|{c.rank.ljust(3)}| "
            rows[2] += f"| {c.suit} | "
            rows[3] += f"|{c.rank.rjust(3, '_')}| "

    for r in rows:
        print(r)


def get_bet(max_bet):
    print(f'How much do you bet? (1-{max_bet}, or QUIT)')
    answer = input('> ')
    while True:
        if answer.isdigit() and int(answer) <= max_bet:
            return int(answer)
        elif answer.lower().strip() == 'quit':
            return None


def get_hand_value(cards: list[Card]):
    total_value = 0
    for c in cards:
        if c.rank in ['J', 'Q', 'K']:
            total_value += 10
        elif c.rank == 'A':
            total_value += 11
        else:
            total_value += int(c.rank)

    ace_count = sum(1 for c in cards if c.rank == 'A')
    for _ in range(ace_count):
        if total_value > 21:
            total_value -= 10

    return total_value






print('Rules...')
balance = INITIAL_DEPOSIT

first_turn  = True
player_lost = False
bet = get_bet(balance)
if bet is None:
    print('Thanks for playing..')
    exit()

balance -= bet

d = Deck()
player = [d.get_card() for _ in range(2)]
dealer = [d.get_card() for _ in range(2)]


# player's turn
while True:
    print(f'Bet: {bet}\n')
    print('DEALER: ???')
    display_cards([BACKSIDE, dealer[1]])
    print(f'PLAYER: {get_hand_value(player)}')
    display_cards(player)

    if first_turn:
        choice = input('(H)it, (S)tand, (D)ouble down>').lower().strip()
    else:
        choice = input('(H)it, (S)tand>').lower().strip()

    if choice == 'd' and first_turn:
        additional_bet = get_bet(balance)
        balance -= additional_bet
        new_card = d.cards.pop()
        print(f'You drew a {new_card.rank} of {new_card.suit}')
        player.append(new_card)

    elif choice == 'h':
        new_card = d.cards.pop()
        print(f'You drew a {new_card.rank} of {new_card.suit}')
        player.append(new_card)

    elif choice == 's':
        break

    if get_hand_value(player) > 21:
        player_lost = True
        break


    first_turn = False


# dealer's turn
if not player_lost:
    while True:
        if get_hand_value(player) > get_hand_value(dealer) < 21:
            dealer.append(d.cards.pop())
        else:
            break



print(f'Bet: {bet}\n')
print(f'DEALER: {get_hand_value(dealer)}')
display_cards(dealer)
print(f'PLAYER: {get_hand_value(player)}')
display_cards(player)

if get_hand_value(player) > 21:
    print('You busted')

elif get_hand_value(dealer) > 21:
    print('Dealer busted')
    balance += 2*bet

elif get_hand_value(player) > get_hand_value(dealer):
    print('You won')
    balance += 2*bet

elif get_hand_value(player) < get_hand_value(dealer):
    print('You lost')

else:
    print("It's a tie")
    balance += bet
