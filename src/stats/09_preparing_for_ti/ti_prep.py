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






# What is the probability that there will be three sailboats in an observation of 5 ships?

# What is the probability of seeing 2 tankers and yacht in an observation of 5 ships?

