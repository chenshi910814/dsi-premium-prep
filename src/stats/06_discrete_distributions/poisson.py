from math import e, factorial

def poisson_pmf(lam, k):
    return (e**(-lam) * lam**k) / factorial(k)

'''
On average, ten people visit the ATM in an hour. What is the probability that 12 people visit the ATM in an hour?
'''
lam = 10
k = 12

print(poisson_pmf(lam, k))