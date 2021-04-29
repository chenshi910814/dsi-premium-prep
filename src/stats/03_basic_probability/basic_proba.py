pets = ['c', 'd', 'f', 'g']

pet_outcomes = []

for pet1 in pets:
    for pet2 in pets:
        for pet3 in pets:
            for pet4 in pets:
                pet_outcomes.append([pet1, pet2, pet3, pet4])

# for pet_outcome in pet_outcomes:
#     print(pet_outcome)

# print(4**4)
# print(len(pet_outcomes))

two_or_more_c = []

# for pet_outcome in pet_outcomes:
#     if pet_outcome.count('c') >= 2:
#         two_or_more_c.append(pet_outcome)

# print(two_or_more_c)

# card_A = len(two_or_more_c)
# card_S = len(pet_outcomes)

# proba_two_or_more_c = card_A / card_S

# print(proba_two_or_more_c)


from random import choice

def coin_flip():
    flip = ['H', 'T']
    return choice(flip)

def series_of_flips(n):
    flips = []

    for _ in range(n):
        flips.append(coin_flip())

    return flips

# print(series_of_flips(4))