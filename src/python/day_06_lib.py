"""un/comment to de/activate ###########################

list1 = [1, 2, 3]
list2 = list1
print( id(list1), list1 )
print( id(list2), list2 )

list1.append(4)
print( id(list1), list1 )
print( id(list2), list2 )

###################################################### """
"""un/comment to de/activate ###########################

list1 = [1, 2, 3]
list2 = list1.copy()
print( id(list1), list1 )
print( id(list2), list2 )

list1.append(4)
print( id(list1), list1 )
print( id(list2), list2 )

###################################################### """
"""un/comment to de/activate ###########################

# types
    # int, float
    # bool
    # str
    # None

    # list

# abstraction
    # variables
    # functions

# control flow
    # if, elif, else
    # bool, conditions

# iteration
    # loops
        # for

###################################################### """
"""un/comment to de/activate ###########################

sqrs_lst = 0
for num in range(10, 20):
    sqrs_lst.append(num**2)

print( sqrs_lst )

###################################################### """
"""un/comment to de/activate ###########################

src = range(10, 50)

perfect_squares_lst = []
counter = 0
for i in src:
    i_sqrt = i**(1/2)
    if i_sqrt == int(i_sqrt):
        perfect_squares_lst.append( [i, i_sqrt] )
        counter += 1

print( perfect_squares_lst )
print( counter )

###################################################### """
"""un/comment to de/activate ###########################

# if i encounter a number divisible by 3
# raise the NEXT number to the power of the prior number

src_lst = [5, 3, 7, 9, 15, 22, 3, 24, 2]

prev = None
flag = False
nums_lst = []
for i in src_lst:
    # iteration: 4
        # i = 9
        # prev = 3
        # flag = False
    if flag:
        flag = False
        nums_lst.append(i**prev)

    if i % 3 == 0:
        flag = True
        prev = i

print(nums_lst)

###################################################### """
"""un/comment to de/activate ###########################

'''
is_prime

args:
    n: <int>

return:
    <bool> returns True if n is prime else False
'''

def is_prime(n):
    if n < 2: return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def is_prime(num):
    prime = True
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    return prime


for i in range(20):
    print(i, is_prime(i))

###################################################### """
"""un/comment to de/activate ###########################

some_list = [4, 5, 2, 7, 8, 6, 7, 5, 7, 1, 2]
accumulator = []
for i in some_list:
    if i > 4:
        accumulator.append(i)

print(accumulator)

###################################################### """
"""un/comment to de/activate ###########################

some_list = [4, 5, 2, 7, 8, 6, 7, 5, 7, 1, 2]
for i in some_list:
    if i < 5:
        continue # skip (skip to the next iteration)

    print(i)

# 5 7 8 6 7 5 7

###################################################### """
"""un/comment to de/activate ###########################

def factorial(n):
    if n < 0:
        raise ValueError(f"factorial of {n} is unefined")
    prod = 1
    for i in range(2, n+1):
        prod *= i

    return prod

print(factorial(-1))
# print(factorial(0))

# for i in range(-2, 6):
#     print(i, factorial(i))

###################################################### """
"""un/comment to de/activate ###########################

# inverted range
print(range(10, 3))
for i in range(10, 3):
    print(i)

###################################################### """
"""un/comment to de/activate ###########################

word_lst = ['Whose', 'woods', 'these', 'are', 'I', 'think', 'I', 'know', 'His', 'house', 'is', 'in', 'the', 'village', 'though', 'He', 'will', 'not', 'see', 'me', 'stopping', 'here', 'To', 'watch', 'his', 'woods', 'fill', 'up', 'with', 'snow']
vwl_word_lst = []
for word in word_lst:
    vwl_word = ""
    for ch in word:
        if ch.lower() in "aeiouy":
            vwl_word += ch

    vwl_word_lst.append(vwl_word)

print(vwl_word_lst)

# ['oe', 'oo', 'ee']
###################################################### """
"""un/comment to de/activate ###########################
# nested accumulator

word_lst = ['Whose', 'woods', 'these', 'are', 'I', 'think', 'I', 'know', 'His', 'house', 'is', 'in', 'the', 'village', 'though', 'He', 'will', 'not', 'see', 'me', 'stopping', 'here', 'To', 'watch', 'his', 'woods', 'fill', 'up', 'with', 'snow']
vwl_word_lst = []
for word in word_lst:
    vwl_word = ""
    for ch in word:
        if ch.lower() in "aeiouy":
            vwl_word += ch

    vwl_word_lst.append(vwl_word)

print(vwl_word_lst)

# ['oe', 'oo', 'ee']

###################################################### """
