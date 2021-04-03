from random import random

# Dependent Sampling


def get_result(prior_res=0):
    rand = random()
    if rand < (0.33 - prior_result * 0.001):
        return 0
    elif rand < 0.66 + prior_result * 0.001:
        return 1
    else:
        return 2

