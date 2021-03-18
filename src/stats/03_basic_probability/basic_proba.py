
pets = ['cat', 'dog', 'ferret', 'goldfish']

'''
Exhaustive set of possibilities for drawing 3 pets WITH REPLACEMENT
'''

pet_outcomes = []

for pet1 in pets:
    for pet2 in pets:
        for pet3 in pets:
            for pet4 in pets:
                pet_outcomes.append([pet1, pet2, pet3, pet4])

# for pet_outcome in pet_outcomes:
#     print(pet_outcome)

two_or_more_cats = []

for pet_outcome in pet_outcomes:
    if pet_outcome.count('cat') >= 2:
        two_or_more_cats.append(pet_outcome)



# for item in two_or_more_cats:
#     print(item)
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

# print(series_of_flips(10000).count('H'))


def four_flip_sample_space():
    flips = ['H', 'T']
    outcomes = []

    for flip1 in flips:
        for flip2 in flips:
            for flip3 in flips:
                for flip4 in flips:
                    outcomes.append([flip1, flip2, flip3, flip4])