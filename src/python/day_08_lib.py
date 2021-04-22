"""un/comment to de/activate ###########################

# types
    # int, float
    # bool
    # None
    # str
    # *tuples

    # list
    # dictionaries

    # *sets

# abstraction
    # variables
    # functions

# control flow
    # if elif else

# iteration
    # for
    # while

    # map

text = '''
Whose woods these are I think I know
His house is in the village though
He will not see me stopping here
To watch his woods fill up with snow
'''
word_list = text.split()
word_list.append(57)
# print(word_list)

back_to_string = " ".join( map(str, word_list) )

print(back_to_string)


#######################################################"""
"""un/comment to de/activate ###########################
# mutable

# key/value pairs in a
# unordered

d = {
    "make" : "toyota",
    "modle": "highlander",
    "color": "black",
    "year" : 2011 }

# print( d["make"] ) # KeyError: 1
# print( d )

# for k, v in d.items():
#     print(k, v)


# car2 = {
#     "make" : "honda",
#     "modle": "accord",
#     "color": "red",
#     "year" : 1994 }
#
# print( car2 )
# print( car1 )

#######################################################"""
"""un/comment to de/activate ###########################

# CRUD
# create
d = {}
d = {"make": "toyota"}
d["modle"] = "highlander" # equal to an append

# read / access
# d["make"]
# d["modle"]
print(d)
some_var = "make"
# if some_var in d.keys():
#     print(d[some_var])
# else:
#     print(some_var, "is not in the dictionary")
res = d.get(some_var, f"{some_var} is not in the dictionary")
print(res)

# update
d["modle"] = "huntsman"

# delete
# del d
# print(d) # NameError: name 'd' is not defined
# del d["modle"]
# print(d.pop("make"))
# print(d)

d = {
    "make" : "toyota",
    "modle": "highlander",
    "color": "black",
    "year" : 2011 }

#######################################################"""
"""un/comment to de/activate ###########################

d = {
    "make" : "toyota",
    "modle": "highlander",
    "color": "black",
    "year" : 2011 }

# print(d)

# membership
# .keys()
# .values()
# .items() # both keys and values
# .copy()

def remove_short_keys(d, key_lim):
    d_copy = d.copy()
    for k, v in d.items():
        if len(k) <= key_lim:
            del d_copy[k] # RuntimeError: dictionary changed size during iteration

    return d_copy


some_d = {
    "make" : "toyota" ,
    "modle": "highlander" ,
    "color": "black" ,
    "year" : 2011 }

print( remove_short_keys(some_d, 4) )
print( some_d )

#######################################################"""
"""un/comment to de/activate ###########################

# tuples
# Tuples are ordered collections
# Tuples are very similar to list with two key differences:
    # Tuples are immutable
    # Tuples are declared using parenthesis
# We can index and slice tuples because they are ordered
# Tuples have two methods associated with them: count and index

tup = (55,)
print( tup )



#######################################################"""
"""un/comment to de/activate ###########################
# CSI

'append',
'extend',
tup = ()
# print( tup )
tup += ("hello",)
tup += ("world", "my", "name", "is", "foo")
# print( tup )
'clear',
tup = ()

'copy',
#

'count',
'index',
'insert',
tup = ('hello', 'world', 'my', 'name', 'is', 'foo')
idx = 1
tup = tup[:idx:] + ("there",) + tup[idx::]

'pop',
idx = 1
res = tup[idx]
tup = tup[:idx:] + tup[idx+1::]
print(tup)

'remove',
# idx = 1
ele = "world"
tup = tup[:tup.index("world"):] + tup[tup.index("world")+1::]
print(tup)

'reverse',
print(tup[::-1])

'sort'
# sorted()

#######################################################"""
"""un/comment to de/activate ###########################

# set([])
# .union()
# .intersection()
# .difference()

#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
