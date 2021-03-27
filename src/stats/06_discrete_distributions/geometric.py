
def geometric_pmf(p, k):
    return p * (1-p)**(k-1)

k = 7
p = 0.5

print(geometric_pmf(p, k))