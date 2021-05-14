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
        print(ship_list)
        three_sailboats.append(ship_list)

# print(len(three_sailboats) / len(possible_five_ships))



# What is the probability of seeing 2 tankers and at least one yacht in an observation of 5 ships?
two_tankers_yacht = []

for ship_list in possible_five_ships:
    if ship_list.count('tanker') == 2 and ship_list.count('yacht') >= 1:
        print(ship_list)
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