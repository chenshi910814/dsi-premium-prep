from math import e

def factorial(n):
    prod = 1
    for num in range(2, n+1):
        prod *= num
    return prod


def poisson_pmf(lam, k):
    return lam**k * e**(-lam) / factorial(k)


# print(poisson_pmf(lam=10, k=12))


def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * (1-p)**(n-k)



lam = 10
k = 10


for n in range(k, 10000):
    print(f'binom: {round(binomial_pmf(n, k, p=(lam/n)), 7)}')
    print(f'poiss: {round(poisson_pmf(lam, k), 7)}')
    print()