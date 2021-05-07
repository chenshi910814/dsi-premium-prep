from math import e, factorial

def poisson_pmf(lam, k):
    return (e ** (-lam) * lam**k) / factorial(k)

# print(poisson_pmf(10, 10))


def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * (1-p)**(n-k)



lam = 10
k = 10


# for n in range(k, 10000):
#     print(f'binom: {round(binomial_pmf(n, k, p=(lam/n)), 7)}')
#     print(f'poiss: {round(poisson_pmf(lam, k), 7)}')
#     print()

# lam = 15 * (15/10)
# k = 20
# print(lam)
# print(poisson_pmf(lam, k))


def poisson_cdf(lam, low_k, high_k):
    proba = 0
    for k in range(low_k, high_k+1):
        proba += poisson_pmf(lam, k)
    return proba

