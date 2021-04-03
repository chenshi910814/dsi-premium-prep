from random import random

# Dependent Sampling


def get_result(prior_res=0):
    rand = random()
    if rand < (0.33 - prior_res * 0.1):
        return 0
    elif rand < 0.66 + prior_res * 0.1:
        return 1
    else:
        return 2

def get_trials(n=12):
    res = get_result()
    lst = [res]

    for _ in range(n-1):
        res = get_result(res)
        lst.append(res)

    return lst


# print(get_trials(n=12))


def process_lst(n=12):
    X = get_trials(n)
    accum = 0.0
    for x in X:
        accum += 1/3 * x
    return accum / n

for _ in range(100):
    print(process_lst())
    input()