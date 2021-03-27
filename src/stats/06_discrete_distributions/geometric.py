
def geometric_pmf(p, k):
    return p * (1-p)**(k-1)

# for k in range(1, 20):
#     p = 0.5

#     print(geometric_pmf(p, k))


'''
You have a series of routers transmitting packets of data. There is a 0.99 probability that a given packet of data passes through the router.

What is the probability that a given packet of data is lost in the 15th router?
'''
p_lost = 0.01
k = 15

# print(geometric_pmf(p_lost, k))


'''
You have a series of routers transmitting packets of data. There is a 0.99 probability that a given packet of data passes through the router.

What is the probability that a given packet of data is lost in or before the 15th router?
'''

p_lost = 0.01
k = 15

def geometric_cdf(p, k_high):
    accum = 0.0
    for k in range(0, k_high+1):
        accum += geometric_pmf(p, k)
    return accum

print(geometric_cdf(p_lost, k))

