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

print(len(two_or_more_cats) / len(pet_outcomes))