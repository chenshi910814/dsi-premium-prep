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




def four_flip_sample_space():
    flips = ['H', 'T']
    outcomes = []

    for f1 in flips:
        for f2 in flips:
            for f3 in flips:
                for f4 in flips:
                    outcomes.append([f1, f2, f3, f4])
    return outcomes

outcomes = four_flip_sample_space()


# What is the probability that in 4 coin flips, you get exactly 3 heads?
A = []

for outcome in outcomes:
    if outcome.count('H') == 3:
        A.append(outcome)

# print(len(A) / len(outcomes))



def ten_flip_sample_space():
    flips = ['H', 'T']
    outcomes = []

    for f1 in flips:
        for f2 in flips:
            for f3 in flips:
                for f4 in flips:
                    for f5 in flips:
                        for f6 in flips:
                            for f7 in flips:
                                for f8 in flips:
                                    for f9 in flips:
                                        for f10 in flips:
                                            outcomes.append([f1, f2, f3, f4, f5, f6, f7, f8, f9, f10])
    return outcomes

# for outcome in ten_flip_sample_space():
#     print(outcome)

# print(1 / (2**10))


def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod

# print(factorial(5))

numbers = [0,1,2,3,4,5,6,7,8,9]

base_ten = []

for num1 in numbers:
    print(num1)
    for num2 in numbers:
        print('  ', num2)
        for num3 in numbers:
            print('    ', num3)
            for num4 in numbers:
                print('      ', num4)
#                 base_ten.append([num1, num2, num3, num4])

# for num in base_ten:
#     print(num)