"""un/comment to de/activate ###########################

# data types
    # int, float
        # + - * / // % **
    # bool
        # == != < > <= >=
        # not, and, or
        # in
    # str
    # None

    # list
        # indexing / subscripting / slicing
        # .append
        # len, range
        # in

# abstraction
    # variables
    # functions

# control flow
    # if elif else
    # condition is any expression that evaluates to True or False

# iteration
    # for
    # while

#######################################################"""
"""un/comment to de/activate ###########################

a = 0     # assaignment and initialization
a = 1     # assaignment or reassaignment
a = a + 1
a += 1
a -= 1
a *= 1
a /= 1
a //= 1
a %= 1

#######################################################"""
"""un/comment to de/activate ###########################

# [3.14, 87, "hello", [1, 2, 3, "hi"]]

lst = [3, 4, 5, 6, 7]
print(lst) # [3, 4, 5, 6, 7]

#######################################################"""
"""un/comment to de/activate ###########################

my_range  = range(10)
my_lst    = list(my_range)
print( "X", my_lst )
print( "Y", my_range )       # Will this line print A. or B.

# A. range(0, 10)
# B. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#######################################################"""
"""un/comment to de/activate ###########################

lst = []
print(lst)
lst.append(5)
lst = [5]
print(lst)

#######################################################"""
"""un/comment to de/activate ###########################

lst = [55, 44, 77, 22, 33, 99, 55, 22]
lst.append("foo")
lst.append("bar")
lst.append("bas")
print( lst[4] )

#######################################################"""
"""un/comment to de/activate ###########################

# len IPO
# input: some type that has a length
# output: int, representing the lenghth of the argument

# range
# input:
    # 1 (stop (exclusive))
        # output: generates a range from 0 - stop
    # 2 (start (inclusive), stop (exclusive))
        # output: generates a range from start - stop
    # 3 (start (inclusive), stop (exclusive), step)
        # output: generates a range from start - stop in "steps" of step

# print( list( range(0, 31, 3) ) )

#######################################################"""
"""un/comment to de/activate ###########################

num_lst = [55, 44, 77, 22, 33, 99, 55, 22]
print(num_lst)
print(len(num_lst))
idx_lst = list(  range( len(num_lst) )  )
print(idx_lst)

#######################################################"""
"""un/comment to de/activate ###########################
# membership
num_lst = [55, 44, 77, 22, 33, 99, 55, 22]

print( 99 in num_lst )

#######################################################"""
"""un/comment to de/activate ###########################

num_lst = [55, 44, 77, 22, 33, 99, 55, 22]
print( num_lst[7] )
# print( num_lst[8] ) # IndexError: list index out of range
# print( num_lst[-9] ) # IndexError: list index out of range
print( num_lst[-8] )
# print( num_lst[-9] )


#######################################################"""
"""un/comment to de/activate ###########################

# slicing
num_lst = [55, 44, 77, 22, 33, 99, 55, 22]
# print( num_lst[1] )
# range - start (inclusive), stop (exclusive), step
print( num_lst[::] ) # [55, 44, 77, 22, 33]

#######################################################"""
"""un/comment to de/activate ###########################

# id
# input:  any obj
# output: the internal ID of that obj
lst = ["hello"]
print( id(lst), lst )
other_lst = lst.copy()
other_lst.append("world")
print( id(lst), lst )
print( id(other_lst), other_lst )

#######################################################"""
"""un/comment to de/activate ###########################


def is_prime(num):
    if num < 2: return False
    for factor in range(2, int(num**.5)+1 ):
        if num % factor == 0:
            return False

    return True


def next_prime(anchor):
    counter = anchor
    while True:
        counter += 1
        if is_prime(counter):
            return counter


def twin_prime(nth):
    '''
    The twin prime conjecture is a theory in which there are an infinite
    number of pairs of primes that differ by 2. This function finds the
    'nth' twin prime pair. For example, the 5th twin prime pair is (29, 31).
    Parameters:
    ---------------
    nth: (int)
        This function finds the 'nth' twin prime pair
    Return:
    ---------------
    list
        The 'nth' pair of twin primes
    '''
    prime_anchor = 2
    pair_counter = 0
    while True:
        prime_anchor = next_prime(prime_anchor)
        if is_prime(prime_anchor + 2):
            pair_counter += 1
            if pair_counter >= nth:
                return [prime_anchor, prime_anchor + 2]


for i in range(15):
    print(i, twin_prime(i) )

#######################################################"""
"""un/comment to de/activate ###########################

def is_prime(num):
    if num < 2: return False
    for factor in range(2,int((num**.5)+1)):
        if num % factor == 0:
            return False
    return True


def next_prime(anchor):
    counter = anchor
    while True:
        counter += 1
        if is_prime(counter):
            return counter


def twin_prime(nth):
    """
    The twin prime conjecture is a theory in which there are an infinite
    number of pairs of primes that differ by 2. This function finds the
    'nth' twin prime pair. For example, the 5th twin prime pair is (29, 31).
    Parameters:
    ---------------
    nth: (int)
        This function finds the 'nth' twin prime pair
    Return:
    ---------------
    list
        The 'nth' pair of twin primes
    """
    prime_anchor = 1
    pair_counter = 1
    while True:
        second_prime = next_prime(prime_anchor)
        if second_prime - prime_anchor == 2:
            if pair_counter >= nth:
                return [prime_anchor, second_prime]

            pair_counter += 1
        prime_anchor = second_prime


#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
