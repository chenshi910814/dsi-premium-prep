from math import e, factorial


def poisson_pmf(lam, k):
    return (e**(-lam) * lam**k) / factorial(k)

'''
On average, ten people visit the ATM in an hour. What is the probability that 12 people visit the ATM in an hour?
'''
lam = 10
k = 12

# print(poisson_pmf(lam, k))

'''
A specific space telescope takes random images of deep space. On average 23 Super Giant stars are seen in an image. What is the probability that two randomly selected images will have a total count of 35 Super Giant stars in them?
'''
lam = 23 * 2
k = 35

# print(poisson_pmf(lam, k))





def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))


def binomial_pmf(n, k, p):
    return combinations(n, k) * p**k * (1-p)**(n-k)



lam = 10
k = 10

# for n_trials in range(k, 10000):
#     print(f'binom: {round(binomial_pmf(n_trials, k, p=(lam/n_trials)), 7)}')
#     print(f'poiss: {round(poisson_pmf(lam, k), 7)}')
#     input()

lam = 15 * (15 / 10)
k = 20

print(poisson_pmf(lam, k))