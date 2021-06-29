from random import choice

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

    for item in lst:
        total += (item - mean_)**2

    return total / (len(lst) - sample)

# print(variance(a)**(1/2))


def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod


# print(factorial(5))

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

