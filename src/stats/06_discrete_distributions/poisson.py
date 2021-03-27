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

# print(poisson_pmf(lam, k))



def poisson_cdf(lam, k_high):
    cdf = 0.0
    for k in range(k_high+1):
        cdf += poisson_pmf(lam, k)
    return cdf


'''
A specific space telescope takes random images of deep space. On average 23 Super Giant stars are seen in an image. What is the probability that two randomly selected images will have a total count of 46 or fewer Super Giant stars in them?
'''

# print(poisson_cdf((2*23), (2*23)))


'''
A given intersection will have, on avg, 15 cars pass through in 10 minutes. What is the probability that more than 15 cars will pass through in 15 minutes?
'''

lam = 15 * (15/10)

# print(1 - poisson_cdf(lam, 15))


def poisson_pmf_dict(lam, low_k, high_k):
    d = dict()

    for k in range(low_k, high_k+1):
        d[k] = poisson_pmf(lam, k)
    return d

d = poisson_pmf_dict(lam=10, low_k=0, high_k=50)

for k, v in d.items():
    print(f'{k}: {round(10000*v, 6)}')

