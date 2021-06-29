from random import choice, random
from math import e

def mean(lst, trim=0):
    lst_ = lst.copy()

    if trim > 0:
        lst_ = sorted(lst_)[trim:-trim]
    return sum(lst_) / len(lst_)

a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]

# print(mean(a, trim=2))


def variance(lst, sample=True):
    mean_ = mean(lst)
    total = 0.0

    for i in range(0, len(lst)):
        total += (lst[i] - mean_)**2

    return total / (len(lst) - sample)

# print(variance(a)**(1/2))


def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod

def factorial_recursive(n):
    if n == 1:
        return n
    else:
        return n * factorial_recursive(n-1)


# print(factorial_recursive(9))

def permutations(n, k):
    return int(factorial(n) / factorial(n-k))

def permutations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return perm

def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))


# print(permutations(5,5))
# print(combinations(5,3))


def proc_list(lst):
    sum_ = 0.0
    for idx, num in enumerate(lst, 1):
        sum_ += num * (1/4)**idx
    return sum_

def get_list(n=8):
    out = []
    fours = [0,1,2,3]
    for _ in range(n):
        out.append(choice(fours))
    return out

lst = get_list()
# print(proc_list(lst), lst)


def bernoulli(p_success=0.5):
    draw = random()
    if draw < p_success:
        return 1
    else:
        return 0

# print(bernoulli(0.3))

def list_of_bits(n_bits):
    bit_list = []
    for _ in range(n_bits):
        bit_list.append([0,1])
    return bit_list

def list_of_bits(n_bits):
    return [choice([0,1]) for _ in range(n_bits)]

# print(list_of_bits(4))


def binary_sampling_dict(num_bits=8, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        bit_sum = sum(list_of_bits(num_bits))
        if bit_sum not in d:
            d[bit_sum] = 0
        d[bit_sum] += 1
    
    return d


# for k, count in sorted(binary_sampling_dict().items()):
#     print(f'{k}: {count}')



def poisson_pmf(lam, k):
    return lam**k  * e**(-lam) / factorial(k)

# print(poisson_pmf(lam=10, k=10))



def poisson_pmf_dict(lam, low_k, high_k):
    d = dict()

    for k in range(low_k, high_k+1):
        d[k] = poisson_pmf(lam, k)
    return d

d = poisson_pmf_dict(lam=10, low_k=0, high_k=20)

for k, v in d.items():
    print(f'{k}: {round(v, 6)}')