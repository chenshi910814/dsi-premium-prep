from random import choice, random


binary = [0, 1]
four_bit_binary = []

for bit1 in binary:
    for bit2 in binary:
        for bit3 in binary:
            for bit4 in binary:
                four_bit_binary.append([bit1, bit2, bit3, bit4])

# for bin_ in four_bit_binary:
#     print(bin_)

def dec_to_bin(dec, n_bits=8):
    bit_list = []
    x = dec

    for _ in range(n_bits):
        bit = x % 2
        bit_list.append(bit)
        x //= 2

    return bit_list[::-1]

# print(dec_to_bin(43, n_bits=8))


def get_binary(n_bits=8):
    bins_d = dict()

    for dec in range(2**n_bits):
        bins_d[dec] = dec_to_bin(dec, n_bits)
        # print(f'{dec}: {bins_d[dec]}')
    return bins_d

# for dec, bin_ in get_binary(n_bits=8).items():
#     print(f'{dec}: {bin_}')



def binomial_distr(n_trials=8):
    binomial_dict = dict()

    bin_dict = get_binary(n_bits=n_trials)

    for _, bin_list in bin_dict.items():
        sum_bits = sum(bin_list)
        if sum_bits not in binomial_dict:
            binomial_dict[sum_bits] = 0
        binomial_dict[sum_bits] += 1

    return binomial_dict

d = binomial_distr(n_trials=12)

# for k, cnt in d.items():
#     print(f'{k}: {cnt}')

'''
What is the probability of 5 heads in 12 coin flips of a fair coin?
n = 12
p = 0.5
'''
# print(d[5] / sum(d.values()))

# for k, cnt in d.items():
#     print(f'{k}: {round(cnt / sum(d.values()), 5)}')


# n = 12
# k = 9
# p = 0.5

# # print(d[9] / sum(d.values()))

# accum = 0.0
# for k in range(0, 4+1):
#     accum += d[k] / sum(d.values())
# print(accum)



def get_bit():
    return choice([0,1])

def generate_n_bits(n=8):
    return [get_bit() for _ in range(n)]
    
    # lst = []
    # for _ in range(n):
    #     lst.append(get_bit())
    # return lst

# print(generate_n_bits(n=8))


def binary_sampling_dict(num_bits=8, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_bits(num_bits)
        num_successes = sum(binary)

        if num_successes not in d:
            d[num_successes] = 1
        else:
            d[num_successes] += 1
        
    return d

# d = binary_sampling_dict(num_bits=64, num_samples=100000)

# for k, cnt in sorted(d.items()):
#     print(f'{k}: {cnt}')

# ''' one trial of 100 samples '''
# d1 = binary_sampling_dict(num_bits=16, num_samples=100)

# for k, v in sorted(d1.items()):
#     print(f'{k}: {v / sum(d1.values())}')
 

# ''' one trial of 1000 samples '''
# d2 = binary_sampling_dict(num_bits=16, num_samples=1000)

# for k, v in sorted(d2.items()):
#     print(f'{k}: {v / sum(d2.values())}')


''' 500 trials of 1000 samples '''

def binary_sampling_clt(n_bits=16, num_samples=1000, num_sample_trials=500):
    d_out = dict()

    for _ in range(num_sample_trials):
        d = binary_sampling_dict(n_bits, num_samples)

        for k, v in d.items():
            if k not in d_out:
                d_out[k] = []
            d_out[k].append(v)

    for k, v in d_out.items():
        d_out[k] = sum(v) / len(v)
    
    return d_out

# d = binary_sampling_clt(n_bits=16, num_samples=1000, num_sample_trials=500)

# # counts
# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')

# # probas
# for k, v in sorted(d.items()):
#     print(f'{k}: {round(v / sum(d.values()), 5)}')




def bernoulli(p_success):
    draw = random()

    if draw < p_success:
        return 1
    else:
        return 0


def generate_n_successes(n=8, p_success=0.1):
    return [bernoulli(p_success) for _ in range(n)]


# print(generate_n_successes(n=8))


def binary_sampling_vary_p(num_bits=8, p=0.5, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_successes(num_bits, p)
        k = sum(binary)

        if k not in d:
            d[k] = 1
        else:
            d[k] += 1
        
    return d

''' one trial of 1000 samples '''
# d = binary_sampling_vary_p(num_bits=8, p=0.333333, num_samples=1000)

# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')


def binary_sampling_clt_vary_p(n_bits=8, p=0.5, num_samples=1000, num_sample_trials=500):
    d_out = dict()

    for _ in range(num_sample_trials):
        d = binary_sampling_vary_p(n_bits, p, num_samples)

        for k, v in d.items():
            if k not in d_out:
                d_out[k] = []
            d_out[k].append(v)

    for k, v in d_out.items():
        d_out[k] = sum(v) / len(v)
    
    return d_out

# d = binary_sampling_clt_vary_p(n_bits=8, p=0.333333, num_samples=1000, num_sample_trials=500)

# # counts
# for k, v in sorted(d.items()):
#     print(f'{k}: {v}')

# # probas
# for k, v in sorted(d.items()):
#     print(f'{k}: {round(v / sum(d.values()), 5)}')





def factorial(n):
    prod = 1
    for num in range(2, n+1):
        prod *= num
    return prod

def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

# print(combinations(5, 2))

def binomial_pmf(n, p, k):
    return combinations(n, k) * p**k * (1-p)**(n-k)

'''
On average 3 out of 5 cars that drive by have an antenna.

What is the probability that out of the next 20 cars,
12 of them have antennae?
'''
n = 20
p = 3/5
# k = 12

# for k in range(n+1):
#     print(k, ': ',binomial_pmf(n, p, k))

# What is the probability in 12 coin flips of a fair coin, that you get 7 heads?
n = 12 
k = 7
p = 0.5

# print(round(binomial_pmf(n, p, k), 4))


# Sitting on a park bench you observe geese walking by. There's a probability of 0.3 that any goose walking by has black feet. What is the probability that 4 out of the next 12 geese walking by has black feet?
n = 12 
k = 4
p = 0.3

# print(round(binomial_pmf(n, p, k), 4))

# At the cat cafe, there is a 40% chance that any one cat you see is a Siberian. What is the probability that 6 out of the 14 cats at the park are Siberian?
n = 14
k = 6
p = 0.4

# print(round(binomial_pmf(n, p, k), 4))


def binomial_cdf(n, k_high, p=0.5):
    accum = 0.0
    for k in range(0, k_high+1):
        accum += binomial_pmf(n, p, k)
    return accum


# At the cat cafe, there is a 40% chance that any one cat you see is a Siberian. What is the probability that 6 or more out of the 14 cats at the cafe are Siberians?
n = 14
k_high = 5
p = 0.4

# print(1 - binomial_cdf(n, k_high, p))


n = 8
p = 0.7
k_high = 2

# print(1 - binomial_cdf(n, k_high, p)) 



def binomial_pmf_dict(n, k_low, k_high, p=0.5):
    d = dict()

    for k in range(k_low, k_high+1):
        d[k] = binomial_pmf(n, p, k)
    
    return d

d = binomial_pmf_dict(n=8, k_low=0, k_high=8, p=0.5)

for k, v in d.items():
    print(f'{k}: {round(v, 6)}')
