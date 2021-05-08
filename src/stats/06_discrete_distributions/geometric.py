from random import random

'''
You're sitting on a park bench.
There is a 0.2 probability that any given 
person walking by is wearing a red hat. What
is the probability that the first person you
see wearing a red hat is the 4th person who 
walks by?
'''
p = 0.2
k_incl = 4
# k_excl = 3

def geometric_pmf(p, k):
    return p * (1-p)**(k-1)

# print(geometric_pmf(p, k_incl))

'''
You are flipping a fair coin. What is the probability that you get your first heads on the 7th flip?
'''
p = 0.5
k_incl = 7

# print(geometric_pmf(p, k_incl))

'''
You have a series of routers transmitting packets of data. There is a 0.99 probability that a given packet of data passes through the router.

What is the probability that a given packet of data is lost in the 15th router?
'''
p = 0.01
k_incl = 15

# print(geometric_pmf(p, k_incl))

def geom_cdf(p, k_high):
    return 1 - (1-p)**k_high

def geometric_cdf(p, k):
    geo_cdf = 1
    for i in range (0, k+1):
        geo_cdf += geometric_pmf(p, k)
    return geo_cdf

# # successfully passing through 14 routers
# print(0.99**14)

# # dropped before 15th
# print(geom_cdf(0.01, 14))
# print(geometric_cdf(0.01, 14))


def geometric_pmf_dict(p, k_high):
    d = dict()

    for k in range(1, k_high+1):
        d[k] = geometric_pmf(p, k)
    
    return d


# d = geometric_pmf_dict(p=0.5, k_high=10)

# for k, v in d.items():
#     print(f'{k}: {v}')


def geometric_cdf_dict(p, k_high):
    d = dict()

    for k in range(1, k_high+1):
        d[k] = geom_cdf(p, k)
    
    return d


# d = geometric_cdf_dict(p=0.5, k_high=1000)

# for k, v in d.items():
#     print(f'{k}: {v}')


def bernoulli(p=0.5):
    if random() < p:
        return 1
    else:
        return 0

def geometric(p=0.5):
    lst = []

    for _ in range(100000000000000000000):
        flip = bernoulli(p)
        lst.append(flip)

        if flip == 1:
            break

    return len(lst)

# print(geometric(p=0.1))


def geometric_samples_dict(p=0.05, num_samples=10000):
    d = dict()

    for _ in range(num_samples):
        num_trials = geometric(p)

        if num_trials not in d:
            d[num_trials] = 0
        d[num_trials] += 1

    return d

# d = geometric_samples_dict(p=0.05, num_samples=100000)

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')

def geometric_samples_trials(p=0.05, num_samples=10000, num_sample_trials=100):
    d_out = dict()
    
    for _ in range(num_sample_trials):
        d = geometric_samples_dict(p, num_samples)

        for k, v in d.items():
            if k not in d_out:
                d_out[k] = []
            d_out[k].append(v)

    for k, lst in d_out.items():
        if len(lst) == 1:
            d_out[k] = lst[0]
            continue
        d_out[k] = round(sum(lst) / len(lst), 5)

    return d_out


# d = geometric_samples_trials(p=0.05, num_samples=10000, num_sample_trials=100)

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')


def geometric_samples_proba_dict(p = 0.05, num_samples=10000, num_sample_trials=100):
    d = geometric_samples_trials(p, num_samples, num_sample_trials)
    d_out = dict()

    for k, v in d.items():
        d_out[k] = v / round(sum(d.values()))

    return d_out

d = geometric_samples_proba_dict(p=0.5, num_samples=10000, num_sample_trials=100)

for k, v in sorted(d.items()):
    print(f'{k}: {round(v, 4)}')