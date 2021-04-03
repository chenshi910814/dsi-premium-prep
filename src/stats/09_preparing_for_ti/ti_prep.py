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
    return (accum / n), X

# for _ in range(100):
#     print(process_lst(n=12))
#     input()


def sample_process(num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        res, X = process_lst(n=12)

        res = round(res, 5)
 
        if res not in d:
            d[res] = [0, []]
        d[res][0] += 1    
        if sorted(X) not in d[res][1]:
            d[res][1].append(sorted(X))
    return d

d = sample_process(num_samples=100000)

for k, v in sorted(d.items()):
    print(f'{k}: {v[0]}')
    for lst in v[1]:
        print('    ',  lst)