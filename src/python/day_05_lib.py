"""un/comment to de/activate ###########################

# data types
    # int, float
    # bool
    # str
    # None

    # list

# abstractions
    # variables
    # functions

# control flow
    # if, elif, else

# iteration
    # for
    # while

#######################################################"""
"""un/comment to de/activate ###########################

'''
Write a function that takes in a number between 0-999:
* Print out whether the number is a single, double, or triple digit number.
* If the number is outside of that range, print a message saying that it is outside of the expected range.
'''

def digit_len(dig):
    dig_str_len = len(str(dig))
    if   dig_str_len == 1:
        return "single"
    elif dig_str_len == 2:
        return "double"
    elif dig_str_len == 3:
        return "tripple"
    else:
        return "the number is outside of the expected range"


print( digit_len(1055) ) # "the number is outside of the expected range"
# print( digit_len(5)    ) # single
# print( digit_len(55)   ) # double
# print( digit_len(555)  ) # triple

#######################################################"""
"""un/comment to de/activate ###########################

# write a function test for a function  called raise_to_power that takes 2 numbers as arguments
# the first argument should be the "base" the number that will be raised
# the second argument should be the "exponent" the number to raise the base by
def raise_to_power(a, b):
    return a**b


def test_raise_to_power(inp, exp):
    res = raise_to_power(*inp)
    print(res == exp, res)

test_raise_to_power( (2, 3), 8)
test_raise_to_power( (2, 5), 32)
test_raise_to_power( (2, 6), 64)

#######################################################"""
"""un/comment to de/activate ###########################

lst = []
# `for` identifier `in` iterable
# print(list(range(1, 5)))
for     num         in  range(1, 5):
    print(num)
    # lst.append(num**2) # process

print(lst)

#######################################################"""
"""un/comment to de/activate ###########################

src_lst = [5, 3, 7, 9, 15, 22, 3]
acc_lst = []
for num in src_lst:
    if num < 8:
        acc_lst.append(num**2)
    else:
        acc_lst.append(num**(1/2))

print(acc_lst)

#######################################################"""
"""un/comment to de/activate ###########################

def vowels_of(letters):
    acc = []
    for ch in letters:
        if ch.lower() in "aeiou":
            acc.append(ch)
    return acc

char_list = ['o', 'r', 'c', 'h', 'i', 'd']
print(vowels_of(char_list))

#######################################################"""
"""un/comment to de/activate ###########################

def list_intersection(l1, l2):
    if len(l1) < len(l2):
        shorter_lst = l1
        longer_lst = l2
    else:
        shorter_lst = l2
        longer_lst = l1

    acc = []
    for el in shorter_lst:
        if el in longer_lst and el not in acc:
            acc.append(el)

    return sorted(acc)


def test_list_intersection(l1, l2, exp):
    res1 = list_intersection(l1, l2)
    res2 = list_intersection(l2, l1)
    print(f'''
########################################
inp = {l1, l2}
exp = {exp}
{res1 == exp}, {res1}
{res2 == exp}, {res2}
########################################
''')

# test_list_intersection([3, 5, 7, 4, 5], [2, 0, 5, 4, 3], [3, 4, 5])
test_list_intersection([3, 5, 7, 4, 5], [2, 0, 5, 4, 3, 7], [3, 4, 5, 7])
#######################################################"""
"""un/comment to de/activate ###########################

src_lst = [5, 3, 7, 9, 15, 22, 3]

counter = 0
for el in src_lst:
    if el > 5:
        counter += 1

print( counter )


def factorial(n):
    prod = 1
    for i in range(2, n+1):
        prod *= i

    return prod


print( factorial(4) ) # 24
# 2 * 3 * 4

#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
