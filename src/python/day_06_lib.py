# """un/comment to de/activate ###########################

# evaluation / execution
# data types
    # int float
    # bool
    # str
    # None

    # list

# abstraction
    # variables
    # functions

# control flow
    # if elif else

# iteration
    # for
    # while

#######################################################"""
"""un/comment to de/activate ###########################

'append'
lst = []
# print( id(lst), lst ) # 139982784809216
lst.append("hello")
lst.append("hello")
lst.append("yo")
# print( lst.append("hi") )
# print( id(lst), lst ) # 139982784809216

'clear'
lst.clear()
# print( id(lst), lst ) # 139982784809216

'copy'
def my_function(some_lst):
    some_lst = some_lst.copy()
    some_lst.clear()
    print(id(some_lst), "some_lst")
    return some_lst


lst = [55, 44, 77]
# print( id(lst), "lst")
# print( my_function(lst) )
# print( lst )
# what's the value of lst
# what should be the value of lst

'count'
# I
    # list method, takes any arbitrary object to be counted in the list
# P
# O
    # int, representing the count of the input in the list
# lst = [44, 55, 33, 44, 22, 99]
# print( lst.count(77) )

'extend'
# lst  = [44, 55, 33, 44, 22, 99]
# lst += [333, 444]
# lst.extend( [333, 444] )
# print(lst)

'index'
# lst = [44, 55, 33, 44, 22, 99]
# print( lst.index(44) )

'insert'
# lst = [44, 55, 33, 44, 22, 99]
# lst.insert(4, "hello")
# print(lst)

'pop'
# lst = [44, 55, 33, 44, 22, 99]
# print( lst.pop() )
# print( lst )

'remove'
# lst = [44, 55, 33, 44, 22, 99]
# lst.remove(44)
# print(lst)

'reverse'
# lst = [44, 55, 33, 44, 22, 99]
# lst.reverse()
# print(lst)
# lst.reverse()
# print(lst)

'sort'
# lst = [44, 55, 33, 44, 22, 99]
# print(id(sorted(lst)))
# print(id(lst))

# item assaignment
# lst = [44, 55, 33, 44, 22, 99]
# print(id(lst), lst)
# lst[2] = "banana"
# print(id(lst), lst)

# len
# lst = [44, 55, 33, 44, 22, 99]
# max_idx = len(lst) - 1
# print( len(lst) )

# sum
# lst = [44, 55, 33, 44, 22, 99]
# print( sum(lst) )
# print( sum(lst) / len(lst) )

# max
# min
# lst = [44, 55, 33, 44, 22, 99]
# print( max(lst) )
# print( min(lst) )

# lst = ["hello", "banana", "tomato", "pineapple", "panda bear", "zebra"]
# print( max(lst) )
# print( min(lst) )

# any
# all
# lst = [0, "", [], 0.0, "hello"]
# print( any(lst) )
# print( all(lst) )

# enumerate
# def raise_to_idx(lst):
#     acc = []
#     for idx, num in enumerate(lst, 1):
#         acc.append(num**idx)
#
#     return acc


# my_lst = [44, 55, 33, 44, 22, 99]
# print( raise_to_idx(my_lst) )
# [1, 55, 1089, 85184, 234256, 9509900499]

# parallel lists
# names = ["Sally", "Jeff", "Billy"]
# ages  = [33, 66, 55]

# for name, age in zip(names, ages):
#     print(f"{name} is {age}")

# unpacking

#######################################################"""
"""un/comment to de/activate ###########################

# lst = [44, 55, 33, 44, 22, 99]

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False

    return True


def next_prime(n):
    while not is_prime(n+1):
        n += 1

    return n + 1

#######################################################"""
"""un/comment to de/activate ###########################

def elem_idxs_d(lst):
    d = {}
    for idx, ele in enumerate(lst):
        if ele not in d.keys():
            d[ele] = []
        d[ele].append(idx)

    return d

print(elem_idxs_d( [44, 55, 77, 44, 33, 44, 22, 44] ))
{ 44: [0, 3, 5, 7], 55: [1], 77: [2], 33: [4], 22: [6] }

#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
