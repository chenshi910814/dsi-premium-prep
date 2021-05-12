from random import choice
from math import e, sqrt, pi


def get_bit():
    return choice([0,1])

def get_binary():
    bit_list = []

    for _ in range(16):
        bit_list.append(get_bit())

    return bit_list

# print(get_binary())

def get_float():
    bin_list = get_binary()

    float_accum = 0.0

    for idx, bit in enumerate(bin_list, 1):
        float_accum += bit * 0.5**idx

    return float_accum, bin_list

# print(get_float())



def exponential_pdf(lam, x):
    if x < 0: return 0
    return lam * e**((-lam) * x)

def exponential_cdf(lam, x):
    if x < 0: return 0
    return 1 - e**((-lam) * x)

def exponential_mean(lam):
    return 1 / lam

def exponential_variance(lam):
    return 1 / lam**2

def exponential_stdev(lam):
    return sqrt(exponential_variance(lam))



# print(1 - exponential_cdf(lam=0.1, x=10))

# print(exponential_mean(lam=0.1))

# print(exponential_variance(lam=0.1))
# print(exponential_stdev(lam=0.1))


def normal_pdf(x=0, mu=0, sigma=1):
    return (1 / (sigma * sqrt(2 * pi))) * e ** ((-1/2) * ((x-mu) / sigma)**2)