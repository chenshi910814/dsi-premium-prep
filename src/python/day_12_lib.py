# """un/comment to de/activate ###########################



#######################################################"""
"""un/comment to de/activate ###########################

import random

def coin_flipper(n):
    d = {"heads": 0,  "tails": 0}
    lst = []
    for _ in range(n):
        flip = random.choice(("H", "T"))
        lst.append(flip)
        if flip == "H":
            d["heads"] += 1
        else:
            d["tails"] += 1

    return d, lst

print( coin_flipper(10) )
# {"heads": 3,  "tails": 7}
# ["T", "T", "H", "T", "H", "H", "T", "T", "T", "T"]

#######################################################"""
"""un/comment to de/activate ###########################

# n: number of "events" (flips)
# p: probability of success in each trial
# k: a specific number of "successes" (tails)

def factorial(n):
    prod = 1
    for i in range( 2, n+1 ):
        prod *= i

    return prod


def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))


def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * ((1 - p)**(n - k))


def binomial_cdf(n, k, p=0.5):
    cdf = 0
    for i in range(k+1):
        cdf += binomial_pmf(n, i, p)

    return cdf

###################################################################

def geometric_pmf(k, p=0.5):
    return ( (1 - p)**(k - 1) ) * p


def geometric_cdf(k, p=0.5):
    return 1 - ( (1 - p)**k )


def geometric_cdf(k, p=0.5):
    cdf = 0
    for i in range(1, k+1):
        cdf += geometric_pmf(i, p)

    return cdf


# print( geometric_cdf(10) )


###################################################################

from math import e as E

def poisson_pmf(lmbda, k):
    return (E**(-lmbda)) * ( (lmbda**k) / factorial(k) )


def poisson_cdf(lmbda, k):
    cdf = 0
    for i in range(k+1):
        cdf += poisson_pmf(lmbda, i)

    return cdf

#######################################################"""
"""un/comment to de/activate ###########################

lst = [ i**2 for i in range(1, 11) ]

# print( lst )

import random
random_number_lst = [ random.randint(1, 99) for _ in range(10) ]

lst = []
for num in random_number_lst:
    if (num > 9 and num < 50) or num == 3):
        lst.append(num**2)

lst = [ num**2 for num in random_number_lst if (num > 9 and num < 50) or num == 3 ]


lst = []
for num in random_number_lst:
    if (num > 9 and num < 50) or num == 3):
        if num % 2 == 0:
            lst.append(num**2)
        elif num % 3 == 0:
            lst.append(num*3)
        else:
            lst.append(num**(1/2))


lst = [
    num**2 if num % 2 == 0 else num*3 if num % 3 == 0 else num**(1/2)
    for num in random_number_lst
    if (num > 9 and num < 50) or num == 3)
    ]

print(lst)


#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
