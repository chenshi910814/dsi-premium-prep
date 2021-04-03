from random import random

# Dependent Sampling


def get_result():
    rand = random()
    if rand < 0.33:
        return 0
    elif rand < 0.66:
        return 1
    else:
        return 2