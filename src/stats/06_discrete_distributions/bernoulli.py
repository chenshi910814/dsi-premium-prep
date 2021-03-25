from random import random

def bernoulli(p_success):
    draw = random()

    print(p_success, draw)
    if draw < p_success:
        return 1
    else:
        return 0


bernoulli(p_success=0.37895465647255966)