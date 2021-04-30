

def factorial(num):
    prod = 1
    for n in range(2, num+1):
        prod *= n
    return prod

# print(1 / factorial(10))


def permutations(n, k):
    return int(factorial(n) / factorial(n-k))

# print(permutations(n=30, k=17))

def permutations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return perm

# print(permutations(n=30, k=17))


n = 10
k = 4
# print(permutations(n, k))


base_5 = ['tennis', 'swimming', 'racquetball', 'basketball', 'soccer']

sports_counting = []

for sp1 in base_5:
    for sp2 in base_5:
        for sp3 in base_5:
            for sp4 in base_5:
                for sp5 in base_5:
                    sports_counting.append([sp1, sp2, sp3, sp4, sp5])

# for sp in sports_counting:
#     print(sp)

sp_perms = []

for sp_number in sports_counting:
    perm = True

    for sp in sp_number:
        if sp_number.count(sp) > 1:
            perm = False
            break

    if perm == True:
        sp_perms.append(sp_number)

# for sp_number in sp_perms:
#     print(sp_number)




'''
Heap's Algorithm
'''

def swap(lst, idx_1, idx_2):
    lst_ = lst.copy()
    temp = lst_[idx_2]
    lst_[idx_2] = lst_[idx_1]
    lst_[idx_1] = temp
    return lst_


def heaps_non_recursive(lst, k):
    lst_copy = lst.copy()

    # holds stack stack
    c = [0] * len(lst)

    # collect perms
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

            # incr the counter
            c[i] += 1

            # reset i
            i = 0
        else:
            c[i] = 0
            i += 1
    
    return perms

# base_5 = ['tennis', 'swimming', 'racquetball', 'basketball', 'soccer']

# base_5_perms = heaps_non_recursive(base_5, k=3)

# for perm in base_5_perms:
#     print(perm)


def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

# print(combinations(21, 5))

def combinations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return int(perm / factorial(k))

# print(combinations(21, 5))

