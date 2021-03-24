
rolls = range(1, 36+1)

suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
card_nums = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
cards = []
for suit in suits:
    for card in card_nums:
        cards.append(f'{card} of {suit}')

# for card in cards:
#     print(card)

flip = ['T', 'H']
coin_flips = []
for flip1 in flip:
    for flip2 in flip:
        for flip3 in flip:
            coin_flips.append([flip1, flip2, flip3])


S = []

for roll in rolls:
    for card in cards:
        for flip in coin_flips:
            S.append([roll, card, flip])



hits = []
for outcome in S:
    if outcome[0] >= 18 and outcome[2].count('H') == 2:
        hits.append(outcome)

# print(f'proba: {round(len(hits) / len(S), 3)}')

from random import choice

def num_attendees():
    num_peeps = 1

    for _ in range(20):
        num_peeps += choice(range(0, 11+1))
    
    return num_peeps

outcomes = dict()

num_samples = 1000000

# for _ in range(num_samples):
#     attending = num_attendees()

#     if attending not in outcomes:
#         outcomes[attending] = 0
#     outcomes[attending] += 1

# for k, v in sorted(outcomes.items()):
#     print(f'{k}: {v}')


total = sum(outcomes.values())
eighty_ninety = 0

# for attendees in range(80, 90+1):
#     eighty_ninety += outcomes[attendees]

# print(f'{round(eighty_ninety / total, 3)}')


from math import pi

def spherical_volume(r):
    return (4/3) * pi * r**3

# print(spherical_volume(4))
# print(spherical_volume(100))

# 268.082573106329
# 4188790.2047863905


def gumball_capacity():
    d = {}

    for r in range(4, 100+1):
        d[r] = int(spherical_volume(r) / spherical_volume(1))

    return d

for r, v in gumball_capacity().items():
    print(f'{r}: {v}')