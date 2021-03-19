
def factorial(n):
    prod = 1
    for num in range(2, n+1):
        prod *= num
    return prod

# print(factorial(5))
# print(factorial(0))


# print(factorial(10))

magn_S = factorial(10)
magn_A = 1

proba = magn_A / magn_S # 2.755731922398589e-07

# print(proba)



def permutations(n, k):
    return int(factorial(n) / factorial(n-k))

def permutations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return perm
    
# print(permutations(500,500))
# print(permutations(3, 2))

'''
Five pets and 5 beds. What are all the ways that you can arrange those 5 pets in 5 beds?
'''

base_5 = ['salamander', 'fish', 'cat', 'dog', 'bird']

animals_counting = []

for an1 in base_5:
    for an2 in base_5:
        for an3 in base_5:
            for an4 in base_5:
                for an5 in base_5:
                    animals_counting.append([an1, an2, an3, an4, an5])

# for an_number in animals_counting:
#     print(an_number)

# print(5**5)
# print(len(animals_counting))

animal_perms = []

for an_number in animals_counting:
    perm = True

    for an in an_number:
        if an_number.count(an) > 1:
            perm = False
            break
    
    if perm:
        animal_perms.append(an_number)

# for an_number in animal_perms:
#     print(an_number)


def swap(lst, idx_1, idx_2):
    lst_ = lst.copy()
    temp = lst_[idx_2]
    lst_[idx_2] = lst_[idx_1]
    lst_[idx_1] = temp
    return lst_


def heaps_non_recursive(lst, k):
    # avoid modifying the param
    lst_copy = lst.copy()

    # hold stack state
    c = [0] * len(lst)

    # collect permutations
    perms = [lst_copy[:k]]

    i = 0 # stack pointer
    while i < len(lst_copy):
        if c[i] < i:
            if i % 2 == 0:
                lst_copy = swap(lst_copy, 0, i)
            else:
                lst_copy = swap(lst_copy, c[i], i)

            if lst_copy[:k] not in perms:
                perms.append(lst_copy[:k])

            # incr counter
            c[i] += 1

            # reset i
            i = 0
        else:
            # reset state of count state at i
            c[i] = 0
            i += 1
    return perms


base_5 = ['salamander', 'fish', 'cat', 'dog', 'bird']

five_p_five = heaps_non_recursive(base_5, 5)

# for five in five_p_five:
#     print(five)

five_p_three = heaps_non_recursive(base_5, 3)

# for three in five_p_three:
#     print(three)


def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

def combinations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return int(perm / factorial(k))

# for k in range(1, 10+1):
#     print(combinations(10, k))


'''
An expensive counting approach

Out of a set of 11 basketball players, only 5 can be on the court at a time. What are all the combinations possible for that basketball team.
'''

num_combs = combinations(11, 5)

def basketball_combs():
    eleven_nums = range(1, 11+1)

    # every arrangement of 5
    possible_five = []

    for i in eleven_nums:
        for j in eleven_nums:
            for k in eleven_nums:
                for l in eleven_nums:
                    for m in eleven_nums:
                        possible_five.append([i,j,k,l,m])

    # for five in possible_five:
    #     print(five)

    perms = []

    for five in possible_five:
        if len(list(set(five))) == 5:
            perms.append(five)

    # for five in perms:
    #     print(five)

    combs = []

    for five in perms:
        sorted_five = sorted(five)
        if sorted_five not in combs:
            combs.append(sorted_five)
    
    return combs

# for five in basketball_combs():
#     print(five)


from random import choice

def basketball_combs_samp(team_size=11, num_players=5):
    combs = []

    player_range = range(1, team_size+1)

    while len(combs) < combination(team_size, num_players):
        player_comb = []

        while len(player_comb) < num_players:
            player_num = choice(player_range)
            if player_num not in player_comb:
                player_comb.append(player_num)

        player_comb = sorted(player_comb)

        if player_comb not in combs:
            print(player_comb)
            combs.append(player_comb)
    return combs

team_size = 11
num_players = 5

print(len(basketball_combs_samp(team_size, num_players)))
print(combinations(teams_size, num_players))