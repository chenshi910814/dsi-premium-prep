from math import e, sqrt

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

def exponential_stdev(lam):
    return sqrt(1 / lam**2)
