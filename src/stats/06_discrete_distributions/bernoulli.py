from random import random

def bernoulli(p_success):
    draw = random()
    if draw < p_success:
        return 1
    else:
        return 0


print(bernoulli(p_success))