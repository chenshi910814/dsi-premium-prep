from math import e, factorial

def poisson_pmf(lam, k):
    return (e ** (-lam) * lam**k) / factorial(k)

print(poisson_pmf(10, 12))