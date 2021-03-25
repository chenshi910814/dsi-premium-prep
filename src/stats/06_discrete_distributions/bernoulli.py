from random import random

def bernoulli(p_success):
    draw = random()

    if draw < p_success:
        return 1
    else:
        return 0


# bernoulli(p_success=0.37895465647255966)


trials = 10000000
true_count = 0
for _ in range(trials):
    if bernoulli(p_success=0.5) == 1:
        true_count += 1

print(round(true_count / trials, 4))