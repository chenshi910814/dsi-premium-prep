
'''
1. Synthesize Outcomes by Counting
'''

rolls = range(1, 36+1)

suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
card_nums = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

cards = []

for suit in suits:
    for card in card_nums:
        cards.append(f'{card} of {suit}')

# print(cards)

coin_flips = []
for flip1 in ['T', 'H']:
    for flip2 in ['T', 'H']:
        for flip3 in ['T', 'H']:
            coin_flips.append([flip1, flip2, flip3])


S = []
for roll in rolls:
    for card in cards:
        for flips in coin_flips:
            S.append([roll, card, flips])




'''
2. Observe/Interpret values in list
'''

# for res in S:
#     print(res)

# print(len(S))


'''
3. Answer Questions/Interpret
'''

hits = []
range_to_hit = 18

for outcome in S:
    if outcome[0] >= range_to_hit and outcome[2].count('H') == 2:
        hits.append(outcome)

f'proba: {round(len(hits) / len(S), 3)}'