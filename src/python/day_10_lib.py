"""un/comment to de/activate ###########################

'''
Write a function called percentile_50 that

takes:
    list of arbitrary numbers

return:
    dictionary
        * keys are strings that describe the upper and lower 50th percentile (the median) as a range (see below)
        * values are lists containing numbers from the input list that fall within the lower(inclusive) or upper(also inclusive) percentile described by the key

'''
def median(lst):
    lst = sorted(lst)
    if len(lst) % 2 != 0: # lst is of odd len
        return lst[ int( len(lst) / 2 ) ]
    else:
        lwr = int( len(lst) / 2 ) - 1
        upr = int( len(lst) / 2 ) + 1
        mids = lst[ lwr : upr ]
        return sum(mids) / 2


def percentile_50(lst):
    med = median(lst)
    d = { '<=0.50': []
        , '>=0.50': []
        }
    for num in lst:
        if num <= med:
            d["<=0.50"].append(num)
        if num >= med:
            d[">=0.50"].append(num)

    return d

'''
Let’s make a function that takes in a list of random numbers (Could be floats or ints) and returns a dictionary which identifies where the numbers appear in terms of quartiles.

* Assume each quartile mark includes the lower end of the range and goes up to but does not include the upper end of the range.
'''

def quartiles(lst):
    d = { '<0.25': []
        , '<0.50': []
        , '<0.75': []
        , '<=1.0': []
        }
    halvs_d = percentile_50(lst)
    lwr = median(halvs_d["<=0.50"])
    med = median(lst)
    upr = median(halvs_d[">=0.50"])
    for num in lst:
        if num < lwr:
            d["<0.25"].append(num)
        elif num < med:
            d["<0.50"].append(num)
        elif num < upr:
            d["<0.75"].append(num)
        else:
            d["<=1.0"].append(num)

    return d

my_lst = [1, 5, 8, 234, 64, 5, 0.1, 44, 746, 9, 10]
print( quartiles(my_lst) )
'''
{ '<=0.50': [1, 5, 8, 5, 0.1, 9]
, '>=0.50': [234, 64, 44, 746, 9, 10]
}

{ '<=0.50': [1, 5, 8, 5, 0.1, 9]
, '>=0.50': [234, 64, 44, 746, 9, 10]
}
'''
# {'<=0.50': [int], '>=0.50': [int]}

# my_lst = [1, 5, 8, 6] # [1, 5, 6, 8]
# print( quartiles(my_lst) )
# my_lst = [1, 5, 8, 5, 7]
# print( quartiles(my_lst) )


#######################################################"""
"""un/comment to de/activate ###########################
import random

def coin_flipper(n):
    d = { "heads": 0
        , "tails": 0
        }
    lst = []
    for _ in range(n):
        flip = random.choice(("heads", "tails"))
        d[flip] += 1
        lst.append(flip[0].upper())

    return d, lst


# whats the probability of getting 7 heads out of 10 flips
def factorial(n):
    prod = 1
    for i in range(2, n+1):
        prod *= i

    return prod


def combinations(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n - r)))


def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * p**k * ( (1 - p)**(n - k) )


print( binomial_pmf(10, 7) )

#######################################################"""
# """un/comment to de/activate ###########################

def median(lst):
    lst = sorted(lst)
    if len(lst) % 2 != 0:#odd
        return lst[int(len(lst) / 2)]#get middle index
    else:#even
    # list of the two median numbers
        mids = lst[int(len(lst) / 2) - 1 : lst(int(len(lst) /2) + 1)]
    return (sum(mids)/2)


def percentile_50(lst):
    my_median = median(lst)
    d = {'<=0.50':[],
         '>=0.50':[],
        }
    if num in lst:
        if num <= med:
            d['<=0.50'].append(num)
        if num >= med:
            d['>=0.50'].append(num)
        return d


def quartiles(lst):
    d = {'<0.25':[], '<0.50': [], '<0.75':[], '<=1.0':[]}
    halves = percentile_50(lst)
    lwr = median(halves["<=0.50"])
    med = median(lst)
    upr = median(halves[">=0.50"])
    for num in lst:
        if num < lwr:
            d['<=0.25'].append(num)
        if num > lwr and num < med:
            d['<=0.50'].append(num)
        if num > med and num < lwr:
            d['>=0.75'].append(num)
        if num > med and num < lwr:
            d['<=1.0'].append(num)
        return d
lst_=[1, 5, 8, 234, 64, 5, 0.1, 44, 746, 9, 10]
print(median(lst_))

#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
