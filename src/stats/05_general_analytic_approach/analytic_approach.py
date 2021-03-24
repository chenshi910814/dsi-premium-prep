
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

print(f'proba: {round(len(hits) / len(S), 3)}')