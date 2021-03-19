
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

for an_number in animal_perms:
    print(an_number)