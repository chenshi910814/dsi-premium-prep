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

# print(1 - exponential_cdf(lam, 10))
# print(exponential_mean(lam))
# print(exponential_variance(lam))
# print(exponential_std(lam))

