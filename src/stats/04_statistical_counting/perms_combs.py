
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

for an_list in animal_perms:
    print(an_list)