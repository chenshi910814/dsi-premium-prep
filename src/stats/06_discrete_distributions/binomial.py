def gen_4_bit_binary():
    bin_dct = dict()
    decimal = 0

    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    bin_dct[decimal] = [i,j,k,l]
                    decimal += 1
    return bin_dct

# for dec, bin_ in gen_4_bit_binary().items():
#     print(f'{dec}: {bin_}')


def dec_to_bin(dec, n_bits=8):
    bin_list = []
    x = dec

    for _ in range(n_bits):
        bit = x % 2
        bin_list.append(bit)
        x //= 2

    return bin_list[::-1] # list(reversed(bin_list))

# print(dec_to_bin(dec=43, n_bits=32))

def get_binary(n_bits=8):
    bins_d = dict()

    for dec in range(2**n_bits):
        bins_d[dec] = dec_to_bin(dec, n_bits)

    return bins_d

# for dec, bin_ in get_binary(n_bits=8).items():
#     print(f'{dec}: {bin_}')


def binomial_distr(n_trials=8):
    binomial_dict = dict()

    bin_dict = get_binary(n_bits=n_trials)

    for _, binary_word in bin_dict.items():
        sum_bits = sum(binary_word)

        if sum_bits not in binomial_dict:
            binomial_dict[sum_bits] = 0
        binomial_dict[sum_bits] += 1
    
    return binomial_dict

d = binomial_distr(n_trials=8)

# for k, v in d.items():
#     print(f'{k}: {v}')

# for k, v in d.items():
#     print(f'{k}: {round(v / sum(d.values()), 5)}')



'''
P(n=12, k=9, p=0.5)
'''
d = binomial_distr(n_trials=12)

# print(round(d[9] / sum(d.values()), 5))

'''
(this is a CDF question)
P(n=12, k <= 4, p=0.5)
'''
proba = 0.0
for k in range(0, 4+1):
    proba += d[k] / sum(d.values())

# print(round(proba, 5))


'''
Sampling
'''

from random import choice

def generate_n_bits(n=8):
    return [choice([0,1]) for _ in range(n)]
    
    # lst = []
    # for _ in range(n):
    #     lst.append(choice([0,1]))
    # return lst

# print(generate_n_bits(n=8))


def binary_sampling_dict(num_bits=8, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_bits(num_bits)
        observed_k = sum(binary)

        if observed_k not in d:
            d[observed_k] = 0
        d[observed_k] += 1
    return d


# ''' one trial of 100 samples '''
# d1 = binary_sampling_dict(num_bits=16, num_samples=100)

# for k, v in sorted(d1.items()):
#     print(f'{k}: {v / sum(d1.values())}')

# ''' one trial of 1000 samples '''
# d2 = binary_sampling_dict(num_bits=16, num_samples=1000)

# for k, v in sorted(d2.items()):
#     print(f'{k}: {v / sum(d2.values())}')


''' 500 trials of 1000 Samples'''

def binary_sampling_clt(n_bits=16, num_samples=1000, num_sample_trials=500):
    d_out = dict()

    for _ in range(num_sample_trials):
        d = binary_sampling_dict(n_bits, num_samples)

        for k, count in d.items():
            if k not in d_out:
                d_out[k] = []
            d_out[k].append(count)

    for k, v in d_out.items():
        d_out[k] = sum(v) / len(v)

    return d_out

# d = binary_sampling_clt(n_bits=16, num_samples=1000, num_sample_trials=500)

# # observe counts
# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')

# print()
# # observe probas
# # observe counts
# for k, v in sorted(d.items()):
#     print(f'{k}: {round(v / sum(d.values()), 5)}')

from random import random

def bernoulli(p_success=0.5):
    if random() < p_success:
        return 1
    else:
        return 0


def generate_n(n=8, p=0.5):
    lst = []
    for _ in range(n):
        lst.append(bernoulli(p))
    return lst

# print(generate_n(n=8, p=0.1))

def binary_sampling_dict_vary_p(num_bits=8, p=0.5, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n(num_bits, p)
        observed_k = sum(binary)

        if observed_k not in d:
            d[observed_k] = 0
        d[observed_k] += 1
    return d

# ''' one trial of 100 samples '''
# d1 = binary_sampling_dict_vary_p(num_bits=8, p=0.3, num_samples=100)

# for k, v in sorted(d1.items()):
#     print(f'{k}: {v / sum(d1.values())}')

# print()

# ''' one trial of 1000 samples '''
# d2 = binary_sampling_dict_vary_p(num_bits=8, p=0.3, num_samples=1000)

# for k, v in sorted(d2.items()):
#     print(f'{k}: {v / sum(d2.values())}')



def binary_sampling_clt_vary_p(n_bits=16, p=0.5, num_samples=1000, num_sample_trials=500):
    d_out = dict()

    for _ in range(num_sample_trials):
        d = binary_sampling_dict_vary_p(n_bits, p, num_samples)

        for k, count in d.items():
            if k not in d_out:
                d_out[k] = []
            d_out[k].append(count)

    for k, v in d_out.items():
        d_out[k] = sum(v) / len(v)

    return d_out

# d = binary_sampling_clt_vary_p(n_bits=8, p=0.3, num_samples=1000, num_sample_trials=500)

# # observe counts
# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')

# print()
# # observe probas
# for k, v in sorted(d.items()):
#     print(f'{k}: {round(v / sum(d.values()), 5)}')





def factorial(n):
    prod = 1
    for num in range(2, n+1):
        prod *= num
    return prod

def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))


def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * (1-p)**(n-k)


'''
What is the proba of getting 7 heads in 12 coin flips?
'''
n = 12
k = 7
p = 0.5

# print(binomial_pmf(n, k, p))

'''
Sitting on a park bench you observe geese walking by. There's a probability of 0.3 that any goose walking by has black feet. What is the probability that 4 out of the next 12 geese walking by has black feet?
'''
n = 12
k = 4
p = 0.3

# print(binomial_pmf(n, k, p))


def binomial_cdf(n, k_high, p=0.5):
    cumulative = 0.0

    for k in range(0, k_high+1):
        cumulative += binomial_pmf(n, k, p)

    return cumulative


'''
The probability that a puppy at the pound is cute is 0.67. What is the probability that 11 or less puppies out of the next 20 you observe at the pound will be cute.
'''

print(binomial_cdf(n=20, k_high=11, p=0.67))

