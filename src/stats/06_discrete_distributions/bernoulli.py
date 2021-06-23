from random import random

def bernoulli(p_success=0.5):
    if random() < p_success:
        return 1
    else:
        return 0



print(bernoulli(0.1))