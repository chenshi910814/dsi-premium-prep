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


for ship_list in possible_five_ships:
    print(ship_list)




# What is the probability that there will be three sailboats in an observation of 5 ships?

# What is the probability of seeing 2 tankers and yacht in an observation of 5 ships?

