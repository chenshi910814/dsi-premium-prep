
def factorial(n):
    prod = 1
    for num in range(2, n+1):
        prod *= num
    return prod

# print(factorial(5))


# print(factorial(10))

# print(1 / factorial(10))


def permutations(n, k):
    return int(factorial(n) / factorial(n-k))

# print(permutations(850, 100))

def permutations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return perm

# print(permutations(850, 100))


base_5 = ['ant', 'bat', 'crawdad', 'eagle', 'falcon']

animals_counting = []

for an1 in base_5:
    for an2 in base_5:
        for an3 in base_5:
            for an4 in base_5:
                for an5 in base_5:
                    animals_counting.append([an1, an2, an3, an4, an5])

# for an in animals_counting:
#     print(an)

animal_perms = []

for an_list in animals_counting:
    perm = True

    for an in an_list:
        if an_list.count(an) > 1:
            perm = False
            break
    if perm:
        animal_perms.append(an_list)

# for an_list in animal_perms:
#     print(an_list)



''' Heaps Algorithm '''

def swap(lst, idx_1, idx_2):
    lst_ = lst.copy()
    temp = lst_[idx_2]
    lst_[idx_2] = lst_[idx_1]
    lst_[idx_1] = temp
    return lst_


# test = [1,2,3,4,5]
# print(swap(test, 0, 2))


def heaps_non_recursive(lst, k):
    # avoid modifying lst
    lst_copy = lst.copy()

    # holds stack state
    c = [0] * len(lst) # -> [0, 0, 0 ...]

    # collect perms, collect initial perm
    perms = [lst_copy[:k]]

    i = 0 # acts like a stack pointer
    while i < len(lst_copy):
        if c[i] < i:
            if i % 2 == 0:
               lst_copy = swap(lst_copy, 0, i)
            else:
                lst_copy = swap(lst_copy, c[i], i)

            if lst_copy[:k] not in perms:
                perms.append(lst_copy[:k])

            # incr the counter
            c[i] += 1

            # reset i
            i = 0
        else:
            # reset state of count state at i
            c[i] = 0
            i += 1
    return perms

base_5 = ['ant', 'bat', 'crawdad', 'eagle', 'falcon']


five_perms = heaps_non_recursive(base_5, 5)

# for five in five_perms:
#     print(five)

# print(len(five_perms))
# print(permutations(5, 5))


def combinations(n, k):
    return int(factorial(n) / (factorial(n-k)*factorial(k)))

# print(combinations(21, 5))

def combinations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return int(perm / factorial(k))

# print(combinations(21, 5))


# an expensive counting approach
'''
Out of 11 basketball players, we can have teams
of 5. How many teams of 5 are possible?
'''



def basketball_combs():
    eleven_nums = range(1, 11+1)

    possible_five = []

    for i in eleven_nums:
        for j in eleven_nums:
            for k in eleven_nums:
                for l in eleven_nums:
                    for m in eleven_nums:
                        possible_five.append([i,j,k,l,m])

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

# num_combs = combinations(11, 5)
# basketball_combs = basketball_combs()

# for comb in basketball_combs:
#     print(comb)

# print(len(basketball_combs))
# print(num_combs)


# an expensive sampling approach
from random import choice

def basketball_combs_samp(team_size=11, num_players=5):
    combs = []

    player_range = range(1, team_size+1)

    while len(combs) < combinations(team_size, num_players):
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


team_size = 21
num_players = 5

print(len(basketball_combs_samp(team_size , num_players)))
print(combinations(team_size, num_players))