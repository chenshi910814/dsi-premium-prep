
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


