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


# for n in range(k, 10000):
#     print(f'binom: {round(binomial_pmf(n, k, p=(lam/n)), 7)}')
#     print(f'poiss: {round(poisson_pmf(lam, k), 7)}')
#     print()


# print(round(poisson_pmf(lam = 15 * (15/10), k=20), 4))


def poisson_cdf(lam, k_high):
    cdf = 0.0

    for k in range(k_high+1):
        cdf += poisson_pmf(lam, k)
    return cdf

# print(15 * (15/10))
# print(1 - poisson_cdf(lam=15 * (15/10), k_high=15))


def poisson_pmf_dict(lam, low_k, high_k):
    d = dict()

    for k in range(low_k, high_k+1):
        d[k] = poisson_pmf(lam, k)
    return d


d = poisson_pmf_dict(lam=22.5, low_k=0, high_k=40)

num_observations = 10000

for k, v in d.items():
    print(f'{k}: {round(v*10000)}')