# """un/comment to de/activate ###########################

# data types
    # int, float
    # bool
    # str
    # None
    # tuple

    # list
    # dict
    # set

# abstraction
    # variables
    # functions
# control flow
    # if elif else
# iteration
    # for
    # while

    # map
    # comprehensions

#######################################################"""
"""un/comment to de/activate ###########################

# sets
'''
Sets are unordered, mutable collections
Sets will only contain unique elements
Sets can be declared:
Using the set constructor set()
'''


#######################################################"""
"""un/comment to de/activate ###########################

set1 = set((1, 2, 3, 4))
set2 = set((3, 4, 5, 6))

print( set1, set2 )
# print( set1.union(set2) )
# print( set2.union(set1) )

# print( set1.intersection(set2) )
# print( set2.intersection(set1) )

# print( set1.difference(set2) )
# print( set2.difference(set1) )

# print( set1 - set2 )
# print( set2 - set1 )

#######################################################"""
"""un/comment to de/activate ###########################
set1 = set('Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.'.lower().replace('.', '').split())
set2 = set('Complex is better than complicated. Flat is better than nested. Sparse is better than dense.'.lower().replace(".", "").split() )

print(set2)

#######################################################"""
"""un/comment to de/activate ###########################
'''
Tuples are ordered collections
Tuples are very similar to lists with two key differences:
    Tuples are immutable.
    Tuples are delimited with parenthesis.

We can index and slice tuples because they are ordered
Tuples have two methods associated with them: count and index
Functions return tuples when returning more than one item
'''

def some_function(x, y):
    return x**2, y**2

print(some_function(4, 7))
# (16, 49)

#######################################################"""
"""un/comment to de/activate ###########################
'''
Dictionaries contain key/value pairs in a mutable, unordered collection.
Keys must be immutable and unique.
Dictionaries are declared:
    * Using curly braces {}
Syntax: {key1 : value1, key2: value2, key3 : value3}
'''

#######################################################"""
"""un/comment to de/activate ###########################

'''
Write a function that prompts the user to input numbers separated by dashes
" - ".

Your script will take those numbers, and return a dictionary where the keys are the inputted numbers, and the values are the squares of those numbers.

Example: If you inputted the numbers "1 - 5 - 8 - 10", your script should print {8: 64, 1: 1, 10: 100, 5: 25} (remember that dictionaries are unordered, which is why the script might print out the key-value pairs in a different order than the user inputted the numbers).
'''

def my_function(num_str):
    d = {}
    for num in num_str.split(" - "):
        num = int( num )
        d[num] = num**2

    return d


arg = "3 - 4 - 75 - 1 - 0 - 9"
print( my_function(arg) )
arg = "1 - 5 - 8 - 10"
print( my_function(arg) )
# {8: 64, 1: 1, 10: 100, 5: 25}
# {1: 1, 5: 25, 8: 64, 10: 100}


#######################################################"""
"""un/comment to de/activate ###########################
'''
Write a function that takes in a string. Return a dictionary where the keys represent unique characters in the string and the values represent the number of times that character appears in the original string. s = 'This is a string, we want you to count how many times each unique character appears in this string!'
'''

def num_chars(s):
    '''
    function that takes in a string and parses through
    identifying how many characters are in each word,
    assuming a whitespace is what separates your words
    parameters:
        s: str - a string

    returns:
        A dictionary, where the keys are the words and the
        values are the number of characters in each word
    '''
    pass



#######################################################"""
"""un/comment to de/activate ###########################
'''
Write a function that takes a string of numbers separated by commas. Your script will then take these numbers and store them as a list of tuples, two at a time. Use the zip() function to do this. If the user inputs an odd number of numbers, then only make a list of the largest number of pairs of two that are possible.
'''
def tuplator(num_str):
    tup_lst = []
    num_lst = num_str.split(", ")
    for l, r in zip(num_lst[0::2], num_lst[1::2]):
        tup_lst.append( (int(l), int(r)) )

    return tup_lst


inp = '1, 2, 3, 4, 5, 6'
exp = [(1, 2), (3, 4), (5, 6)]
res = tuplator(inp)
print(res == exp, res)

inp = '1, 2, 3, 4, 5'
exp = [(1, 2), (3, 4)]
res = tuplator(inp)
print(res == exp, res)


#######################################################"""
"""un/comment to de/activate ###########################

def tuplator(num_str):
    tup_lst = []
    num_lst = num_str.split(", ")
    for l, r in zip(num_lst[0::2], num_lst[1::2]):
        tup_lst.append( (int(l), int(r)) )

    return tup_lst

lst = [4, 3, 5]
print(  [ i**2 for i in lst ]  )

#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
