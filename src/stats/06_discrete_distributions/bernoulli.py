from random import random

def bernoulli(p_success=0.5):
    draw = random()

    if draw < p_success:
        return True
    else:
        return False

trials = 10_000_000
# print([bernoulli(p_success=0.5) for _ in range(trials)].count(True) / trials)

true_count = 0
for _ in range(trials):
    if bernoulli(p_success=0.5) == True:
        true_count += 1
# print(true_count / trials)