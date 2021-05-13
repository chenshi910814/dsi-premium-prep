# """un/comment to de/activate ###########################

# evaluate / execution
# types
    # int, float
    # bool
    # None
    # str
    # tuple

    # list
    # dict
    # sets

# abstraction
    # variables
    # functions

# control flow / conditions
    # if elif else

# iteration
    # for
    # while

    # map
    # comprehensions
        # list
        # dictionary


#######################################################"""
"""un/comment to de/activate ###########################

# def
# invocation

# 1. think the definition does something

# 2. the parameter has no value until you invoke the function

# 3. print != return

def factorial(n):
    prod = 1
    for i in range(2, n+1):
        prod *= i

    return prod


res = factorial(4) + 20
print( res )

#######################################################"""
# """un/comment to de/activate ###########################

'''
Write a function called percentile_50 that takes a list of arbitrary numbers The function will return a dictionary
    * keys are strings that describe the upper and lower 50th percentile (the median) as a range (see below)

    * values are lists containing numbers from the input list that fall within the lower(inclusive) or upper(also inclusive) percentile described by the key
'''
def median(lst):
    lst = sorted(lst)
    if len(lst) % 2 == 1:
        return float(lst[ int(len(lst) / 2) ])
    else:
        return (lst[ int(len(lst) / 2) ] + lst[ int(len(lst) / 2) - 1 ]) / 2


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


def quartiles(lst):
    med = median(lst)
    p50_d = percentile_50(lst)
    p25 = median( p50_d["<=0.50"] )
    p75 = median( p50_d[">=0.50"] )
    d = { "< 0.25": []
        , "< 0.50": []
        , "< 0.75": []
        , "< 1.00": []
        }

    for num in lst:
        if   num < p25:
            d["< 0.25"].append(num)
        elif num < med:
            d["< 0.50"].append(num)
        elif num < p75:
            d["< 0.75"].append(num)
        else:
            d["< 1.00"].append(num)

    return d


inp = [1, 5, 8, 234, 64, 5, 0.1, 44, 746, 9, 10]
res = quartiles(inp)
exp = { '< 0.25': [1, 0.1]
      , '< 0.50': [5, 8, 5]
      , '< 0.75': [44, 9, 10]
      , '< 1.00': [234, 64, 746]
      }
print(res == exp, res)


# inp = [43]
# res = percentile_50(inp)
# exp = {'<=0.50': [1, 5, 8, 5, 0.1, 9], '>=0.50': [234, 64, 44, 746, 9, 10]}
# print(res == exp, res)

# inp = [1, 5, 8, 234, 64, 5, 0.1, 44, 9, 10]
# res = percentile_50(inp)
# exp = {'<=0.50': [1, 5, 8, 5, 0.1, 9], '>=0.50': [234, 64, 44, 746, 9, 10]}
# print(res == exp, res)

#######################################################"""
# """un/comment to de/activate ###########################

# print( random.randint(3, 6) ) # returns an integer within the range given fairly
# print( random.random() ) # returns an float between 0 and 1
# print( random.choice(("hello", 475, 3, 9, 8)) ) # takes in choices and returns a choice fairly

import random
def coin_flipper(n):
    d = {'heads': 0, 'tails': 0}
    choice_lst = []
    for _ in range(n):
        flip = random.choice( ("H", "T") )
        choice_lst.append(flip)
        if flip == "H":
            d["heads"] += 1
        else:
            d["tails"] += 1

    return d, choice_lst


print( coin_flipper(5) )
# {'heads': 3, 'tails': 2}, ["H", "T", "H", "H", "T"]


#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
