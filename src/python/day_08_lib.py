# """ un/comment to de/activate ################

# types
    # strings
    # tuples

    # list
    # dict
    # set

# functions
# conditions
# loops

########################################## """
""" un/comment to de/activate ################

'''
Write a function that prompts the user to input numbers separated by dashes ( - ).

Your script will take those numbers, and print a dictionary where the keys are the inputted numbers,

and the values are the squares of those numbers.

Example: If you inputted the numbers '1 - 5 - 8 - 10', your script should print {8: 64, 1: 1, 10: 100, 5: 25} (remember that dictionaries are unordered, which is why the script might print out the key-value pairs in a different order than the user inputted the numbers).
'''
def square_dict(num_string):
    num_lst = num_string.split(" - ")
    d = {}
    for num in num_lst:
        d[int(num)] = int(num)**2

    return d


inp = '1 - 5 - 8 - 10'
print( square_dict(inp) ) # {8: 64, 1: 1, 10: 100, 5: 25}

########################################## """
""" un/comment to de/activate ################
# tuples

# list methods
'append'
'clear'
# tup = ('hello', 'hello')
# tup = ()
'copy'

'count'

'extend'
tup = ("hello", "more", "stuff")

'index'
'insert'
tup = tup[:1:] + ("hey",) + tup[1::]
print(tup)

'pop'
'remove'
'reverse'
'sort'

#
'count'
'index'

tup = ()
# print(id(tup), tup)
tup += ("hello",)
tup2 = tup
tup += ("hello",)
# print(id(tup), tup)
# print(id(tup2), tup2)

########################################## """
""" un/comment to de/activate ################
# set
set1 = set([33, 5, 22, 7, 44])
set2 = set([55, 5, 22, 7, 410])
print( set1.union(set2) )
print( set1.intersection(set2) )
print( set1.differenc(set2) )
print( set2.differenc(set1) )

my_set = set()
my_set.add()

########################################## """
""" un/comment to de/activate ################

lst = []
print(lst)
# my_set = { [33,4,5,7] } # TypeError: unhashable type: 'list'
my_set = set([33, 4, 5, 7]) # TypeError: unhashable type: 'list'
print(my_set)
lst = my_set
print(lst)


# {33, 44}
my_set = {}
my_set.add("hello")
# AttributeError: 'dict' object has no attribute 'add'

########################################## """
""" un/comment to de/activate ################

def my_function():
    '''
    this is my documentation
    here is the doc stuff
    '''

help(my_function)

########################################## """
""" un/comment to de/activate ################

names           = ["Sally", "Bob", "Jill"]
favorite_colors = ["red", "black", "blue"]
for name, color in zip(names, favorite_colors):
    print(f"{name}'s favorite color is {color}")

########################################## """
""" un/comment to de/activate ################

def tupleizer(num_string):
    num_lst = list(map(int, num_string.split(", ")))
    return list(zip(num_lst[::2], num_lst[1::2]))

print(tupleizer('1, 2, 3, 4, 5, 6')) # [(1, 2), (3, 4), (5, 6)]
print(tupleizer('1, 2, 3, 4, 5'))    # [(1, 2), (3, 4)]

########################################## """
# """ un/comment to de/activate ################

# types
# functions
# conditions
# iterators
    # while
    # for
    # comprehensions
        # list
        # dict

lst = []
for num in [5, 3, 4, 2, 6]:
    lst.append(num**2)
print(lst)


lst = [ num**2 for num in [5, 3, 4, 2, 6] ]
print(lst)

28_345_702_983_475

########################################## """
# """ un/comment to de/activate ################



########################################## """
