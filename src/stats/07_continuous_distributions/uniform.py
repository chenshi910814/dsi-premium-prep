from math import e, sqrt

from random import choice

def get_bit():
    return choice([0,1])

def get_binary(n=8):
    return [get_bit() for _ in range(n)]

def get_float(num_bits=8):
    bin_ = get_binary(num_bits)
    flt = 0.0
    for expon, bit in enumerate(bin_, 1):
        flt += 0.5**expon * bit
    return flt

# print(get_float(16))
    
# print(get_binary())

def exponential_pdf(lam, x):
    if x < 0: return 0
    return lam * e**(-lam * x)

def exponential_cdf(lam, x):
    if x < 0: return 0
    return 1 - e**(-lam * x)

def exponential_mean(lam):
    return 1 / lam

def exponential_variance(lam):
    return 1 / lam**2

def exponential_std(lam):
    return sqrt(exponential_variance(lam))



lam = 0.1

print(1 - exponential_cdf(lam, 10))
print(exponential_mean(lam))
print(exponential_variance(lam))
print(exponential_std(lam))