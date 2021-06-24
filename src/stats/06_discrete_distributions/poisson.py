from math import e

def factorial(n):
    prod = 1
    for num in range(2, n+1):
        prod *= num
    return prod


def poisson_pmf(lam, k):
    return lam**k * e**(-lam) / factorial(k)


print(poisson_pmf(lam=10, k=12))