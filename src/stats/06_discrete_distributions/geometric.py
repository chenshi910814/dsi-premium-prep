
def geometric_pmf(p, k):
    return p * (1-p)**(k-1)

for k in range(1, 20):
    p = 0.5

    print(geometric_pmf(p, k))