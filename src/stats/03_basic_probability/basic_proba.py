pets = ['cat', 'dog', 'fish', 'rat']

pet_outcomes = []

for pet1 in pets:
    for pet2 in pets:
        for pet3 in pets:
            for pet4 in pets:
                pet_outcomes.append([pet1, pet2, pet3, pet4, ])

'''What is the probability that a person will select 2 or more cats when randomly choosing 4 pets (with replacement)?
'''
two_or_more_cats = []
for pet_outcome in pet_outcomes:
    if pet_outcome.count('cat') >= 2:
        two_or_more_cats.append(pet_outcome)

# print(len(two_or_more_cats) / len(pet_outcomes))

from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)

def series_of_flips(n):
    flips = []
    for _ in range(n):
        flips.append(coin_flip())
    return flips


# print(series_of_flips(n=12))

def four_flip_sample_space():
    flips = ['H', 'T']
    outcomes = []

    for flip1 in flips:
        for flip2 in flips:
            for flip3 in flips:
                for flip4 in flips:
                    outcomes.append([flip1, flip2, flip3, flip4, ])

    return outcomes

outcomes = four_flip_sample_space()


three_heads = []
for outcome in outcomes:
    if outcome.count('H') == 3:
        three_heads.append(outcome)

print(len(three_heads) / len(outcomes))