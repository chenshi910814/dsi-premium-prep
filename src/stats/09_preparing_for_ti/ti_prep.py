'''
We're observing ships on a bay. We see 5 types of ships: tankers, sailboats, yachts, cruise ships, transport.

There are rules in the bay that tankers cannot follow or precede cruise ships or yachts. Sailboats cannot precede or follow transport ships.
'''

ships = ['tanker', 'sailboat', 'yacht', 'cruise ship', 'transport ship']

five_ships = []

for ship1 in ships:
    for ship2 in ships:
        for ship3 in ships:
            for ship4 in ships:
                for ship5 in ships:
                    five_ships.append([ship1, ship2, ship3, ship4, ship5])


possible_five_ships = []

for ship_list in five_ships:
    valid = True

    for i, ship in enumerate(ship_list):
        if ship == 'tanker':
            if i == 0:
                if ship_list[i+1] in ['yacht', 'cruise ship']:
                    valid = False
            elif i == 4:
                if ship_list[i-1] in ['yacht', 'cruise ship']:
                    valid = False
            else:
                if ship_list[i+1] in ['yacht', 'cruise ship'] or ship_list[i-1] in ['yacht', 'cruise ship']:
                    valid = False
        if ship == 'sailboat':
            if i == 0:
                if ship_list[i+1] == 'transport ship':
                    valid = False
            elif i == 4:
                if ship_list[i-1] == 'transport ship':
                    valid = False
            else:
                if ship_list[i+1] == 'transport ship' or ship_list[i-1] == 'transport ship':
                    valid = False
    if valid:
        possible_five_ships.append(ship_list)


# for ship_list in possible_five_ships:
#     print(ship_list)


# What is the probability that there will be three sailboats in an observation of 5 ships?
three_sailboats = []

for ship_list in possible_five_ships:
    if ship_list.count('sailboat') == 3:
        # print(ship_list)
        three_sailboats.append(ship_list)

# print(len(three_sailboats) / len(possible_five_ships))



# What is the probability of seeing 2 tankers and at least one yacht in an observation of 5 ships?
two_tankers_yacht = []

for ship_list in possible_five_ships:
    if ship_list.count('tanker') == 2 and ship_list.count('yacht') >= 1:
        # print(ship_list)
        two_tankers_yacht.append(ship_list)

# print(len(two_tankers_yacht) / len(possible_five_ships))


'''
Write a function called dice_roll
has one parameter: num_sides
should return a random side from the roll of the n-sided die
'''
from random import choice

def dice_roll(num_sides):
    return choice(range(1, num_sides+1))

    

'''
Write a function called series_of_rolls, taht takes a list
called dice_sides as a parameter. The list should contain
the sides of the dice that will used in subsequent rolls.

The function should return the list of rolls, in order

ex: the list of dice_sides could look like:
[6, 12, 24, 8, 4]

the returned list could look like:
[3, 12, 4, 7, 2]
'''

def series_of_rolls(dice_sides):
    lst = []
    for sides in dice_sides:
        lst.append(dice_roll(sides))
    return lst

# sides = [6, 12, 24, 8, 4, 64]

# print(series_of_rolls(sides))


'''
You are modeling interactions between bacteria
in an experimental environment. The bacteria
have a series of characteristics that will 
detm whether or not they survive when they 
interact with another bacteria. These characteristics
are represented by a series of dice rolls that will 
be output as a list.

The lengths of the bacteria lists will be the same.

bac_1 has these attribs:
[6, 8, 9, 12, 2, 1]

bac_2 has these attribs:
[2, 18, 20, 5, 1, 2]

Scores: 
bac_1 : 3
bac_2 : 1

bac_1 lives, bac_2 dies
if scores are equal, both bac die
'''

def bacteria_war(bac_1_attr, bac_2_attr):
    bac_1 = series_of_rolls(bac_1_attr)
    bac_2 = series_of_rolls(bac_2_attr)

    score_lst = []
    for i in range(len(bac_1)):
        if bac_1[i] > bac_2[i]:
            score_lst.append(1)
        elif bac_1[i] < bac_2[i]:
            score_lst.append(2)
        else:
            score_lst.append(0)

    if score_lst.count(1) > score_lst.count(2):
        return bac_1_attr
    elif score_lst.count(1) < score_lst.count(2):
        return bac_2_attr
    else:
        return [1] * len(bac_1)


bac_1 = [6, 8, 9, 12, 2, 1]
bac_2 = [2, 18, 20, 5, 1, 2]

# print(bacteria_war(bac_1, bac_2))

def bacteria_war_outcomes(bac_1_attr, bac_2_attr, num_samples=1000):
    d = {
        'bac 1 wins': 0,
        'bac 2 wins': 0,
        'both die  ': 0
    }

    for _ in range(num_samples):
        res = bacteria_war(bac_1_attr, bac_2_attr)

        if res == bac_1_attr:
            d['bac 1 wins'] += 1
        elif res == bac_2_attr:
            d['bac 2 wins'] += 1
        else:
            d['both die  '] += 1
    return d

bac_1 = [6, 8, 9, 12, 2, 1]
bac_2 = [2, 18, 20, 5, 1, 2]

# d = bacteria_war_outcomes(bac_1, bac_2, num_samples=10000)

# for k, v in d.items():
#     print(f'{k}: {v}')



'''
Y is the result of rolling a 4-sided die, then a 7-sided die,
then a 12-sided die, and processing through this function:

Y = (d4**3 + d7**2) * d12**(1/2) 
'''
def roll_math(roll_list):
    d4, d7, d12 = roll_list
    return (d4**3 + d7**2) * d12**(1/2)


'''
What is the probability that:
P(Y <= 80) = ?

P(Y > 50) = ?
'''

''' use counting '''
outcomes_Y = []

for d4 in range(1, 4+1):
    for d7 in range(1, 7+1):
        for d12 in range(1, 12+1):
            outcomes_Y.append(roll_math([d4, d7, d12]))

# for lst in outcomes_Y:
#     print(lst)


lte_80 = 0
gt_50 = 0

for val in outcomes_Y:
    if val <= 80:
        lte_80 += 1
    if val > 50:
        gt_50 += 1

# print('lte_80', round(lte_80 / len(outcomes_Y), 3))
# print('gt_50', round(gt_50 / len(outcomes_Y), 3))

'''
get min and max
'''

def get_min_max(lst):
    return min(lst), max(lst)

# print(get_min_max(outcomes_Y))


def bins_dict(outcomes_Y):
    d = dict()

    for num in range(0, 401, 10):
        if num==0: continue
        d[f'{num-9} to {num}'] = 0

    for val_ in outcomes_Y:
        val = round(val_)

        for k, v in d.items():
            low, _, high = k.split()

            if val >= int(low) and val <= int(high):
                d[k] += 1

    return d


# for k, v in bins_dict(outcomes_Y).items():
#     print(f'{k}: {v}')


bac_1_attributes= [6,8,9,12,2,1]
bac_2_attributes= [2,18,20,5,1,2]

def bacteria_war(bac_1_attributes, bac_2_attributes):
    bac_1 = series_of_rolls(bac_1_attributes)
    bac_2 = series_of_rolls(bac_2_attributes)
    score_lst = []
    for i in range(len(bac_1)):
        if bac_1[i] > bac_2[i]:
            score_lst.append(1)
        elif bac_1[i] < bac_2[i]:
            score_lst.append(2)
        else:
            score_lst.append(0)
    if score_lst.count(1) > score_lst.count(2):
        return "Bacteria 1 wins!!!"
    elif score_lst.count(1) < score_lst.count(2):
        return "Bacteria 2 wins!!!"
    else:
        return "Tie....."

# print(bacteria_war(bac_1_attributes, bac_2_attributes))

def bacteria_war_outcomes(bac_1_attributes, bac_2_attributes, num_samples):
    d = {
        'bac 1 wins': 0,
        'bac 2 wins': 0,
        'both die  ': 0
    }
    for _ in range(num_samples):
        res = bacteria_war(bac_1_attributes, bac_2_attributes)
        if res == "Bacteria 1 wins!!!":
            d['bac 1 wins'] += 1
        elif res == "Bacteria 2 wins!!!":
            d["bac 2 wins"] += 1
        else:
            d['both die  '] += 1
    return d
d = bacteria_war_outcomes(bac_1_attributes, bac_2_attributes, 1000)
for k, v in d.items():
    print(f'{k}: {v}')