from random import random

def bernoulli(p_success=0.5):
    if random() < p_success:
        return 1
    else:
        return 0


# print(bernoulli(0.1))

trials = 10000000
lst = []
for _ in range(trials):
    lst.append(bernoulli(p_success=0.1))

print(lst.count(1) / trials)