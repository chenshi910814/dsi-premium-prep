from math import e, factorial
from binomial import combinations, binomial_pmf

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



print(binomial_pmf(10, .5, 5))