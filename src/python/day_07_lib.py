"""un/comment to de/activate ###########################

iterable
accumlator = some_empty_val
for item in iterable:
    if condition:
        accumlator.modify()
    accumlator.modify()

finish

#######################################################"""
"""un/comment to de/activate ###########################

word_lst = ['Whose', 'woods', 'these', 'are', 'I', 'think', 'I', 'know', 'His', 'house', 'is', 'in', 'the', 'village', 'though', 'He', 'will', 'not', 'see', 'me', 'stopping', 'here', 'To', 'watch', 'his', 'woods', 'fill', 'up', 'with', 'snow']
# vwl_word_lst = []
# for word in word_lst:
#     vwl_word = ""
txt = '''
Whose woods these are I think I know
His house is in the village though
He will not see me stopping here
To watch his woods fill up with snow
'''
vwl_word = ""
for ch in txt:
    if ch.lower() in "aeiouy":
        vwl_word += ch

print(vwl_word)
    # vwl_word_lst.append(vwl_word)

# print(vwl_word_lst)

# ['oe', 'oo', 'ee']

#######################################################"""
"""un/comment to de/activate ###########################
'''
* write a function called sum_evens that will sum all even numbers in a list

before you start:
    what should the function take as an argument?
    what should it return
    write a test or 2 before you start defining the function
'''
def sum_evens(nums):
    acc = 0
    for num in nums:
        if num % 2 == 0:
            acc += num

    return acc

print( sum_evens([3, 7, 5, 6, 9, 8, 1, 4]) ) # 18
print( sum_evens(range(7, 15)) ) # 44

#######################################################"""
"""un/comment to de/activate ###########################

# types
    # int, float
    # ...

    # list <<<<<

# abstractions
    # variables
    # functions
    # classes
        # methods

# control flow
# iteration

#######################################################"""
"""un/comment to de/activate ###########################
# CRUD


#######################################################"""
"""un/comment to de/activate ###########################

lst = []
print(lst)

# appending # create new value
str1 = "hello"
print( lst.append("hello") )
lst.append("world")
a = 10
b = 19
lst.append( (a**2 + b**2)**(1/2) )
lst.append("hello", "world")
# TypeError: append() takes exactly one argument (2 given)

print(lst)
#######################################################"""
"""un/comment to de/activate ###########################
#
lst1 = ["hello"]
print("lst1:", lst1)

lst2 = ["there", "world"]
print("lst2:", lst2)

# extending # create several new value
lst1.append( ["there", "world"] )
# lst1.extend( "there", "world" )
# TypeError: extend() takes exactly one argument (2 given)
print("lst1:", lst1)
print("lst2:", lst2)

#######################################################"""
"""un/comment to de/activate ###########################

lst1 = ["hello"]
print("lst1:", lst1)

lst2 = ["there", "world"]
print("lst2:", lst2)

# extending # create several new value
lst1.extend( ["there", "world"] )
# lst1.extend( "there", "world" )
# TypeError: extend() takes exactly one argument (2 given)
print("lst1:", lst1)
print("lst2:", lst2)

#######################################################"""
"""un/comment to de/activate ###########################
# removing / pop # delete
lst = ["hello", "there", "world", "there"]
print("before, lst:", lst)
# lst.remove("there") # removes first occurence of value passed
res = lst.pop(2)
print("after,  lst:", lst)
print("res:", res)

#######################################################"""
"""un/comment to de/activate ###########################

# len
# sum
lst = [4, 3, 6]
print( len(lst) )
print( sum(lst) )
# print( sum([4, 3, 6, "hello"]) )
# print( sum(["hello", " ", "world"]) )
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

#######################################################"""
"""un/comment to de/activate ###########################
# UPDATE*
# sort
# lst = [4, 3, 6]
# print("before, lst:", lst)
# print(lst.sort()) # None     <<<<<<<<<<<<<<<<<<<<<<<
# print("after,  lst:", lst)

# sorted
# lst = [4, 3, 6]
# print("before, lst:", lst, id(lst) )
# lst = sorted(lst)
# # print(sorted(lst)) # [3, 4, 6] <<<<<<<<<<<<<<<<<<<<<<<
# print("after,  lst:", lst, id(lst) )

#######################################################"""
"""un/comment to de/activate ###########################

# reverse
# lst = [4, 3, 6]
# print("before, lst:", lst)
# print(lst.reverse()) # None     <<<<<<<<<<<<<<<<<<<<<<<
# print("after,  lst:", lst)

# reversed
lst = [4, 3, 6]
print("before, lst:", lst)
print( reversed(lst) ) # None     <<<<<<<<<<<<<<<<<<<<<<<
print("after,  lst:", lst)

#######################################################"""
"""un/comment to de/activate ###########################
# enumerate
src_lst = [4, 5, 3, 8, 9, 9, 7, 0, 1]
acc_lst = []
for idx, num in enumerate(src_lst):
    acc_lst.append(num**idx)

print(acc_lst)

#######################################################"""
"""un/comment to de/activate ###########################

# .count()
# zip()
# unpacking

# max()
# min()
# any()
# all()

# 'append',
# 'clear',
# 'copy',
# 'count',
# 'extend',
# 'index',
# 'insert',
# 'pop',
# 'remove',
# 'reverse',
# 'sort'

#######################################################"""
"""un/comment to de/activate ###########################

my_lst = [4, 52, 8, 3]
print(my_lst)
del my_lst
# print(my_lst) # NameError: name 'my_lst' is not defined

#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
