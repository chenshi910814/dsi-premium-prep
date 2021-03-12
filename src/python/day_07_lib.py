"""un/comment to de/activate ###########################

# types
    # imutable
        # int, float
        # bool
        # str
        # *tuples
        # None

    # mutable
        # list
        # *dict
        # **sets

# functions
    # def discribes a generally form
    # envoke with specific values for the inputs

# conditions
    # if elif else

# loops
    # iterate
    # for, while
    # accumulator

#######################################################"""
# """un/comment to de/activate ###########################

'there\'s' # pythonic
"there's"  # my preference

'''
this
is
a
string
'''
"""
this
is
a
string
"""


#######################################################"""
"""un/comment to de/activate ###########################

name = "Clark"
print("hello " + name)
print("hello " * 2)

#######################################################"""
"""un/comment to de/activate ###########################

for c in str(4897):
    print( c / 2 )
    # TypeError: unsupported operand type(s) for /: 'str' and 'int'


#######################################################"""
"""un/comment to de/activate ###########################

print(        44.5   / 2 )
print( float("44.5") / 2 )

#######################################################"""
"""un/comment to de/activate ###########################

my_name = "Clark"
my_favortie_number = 6
print(my_name + "'s favroite number is " + str(my_favortie_number))
# TypeError: can only concatenate str (not "whatere type") to str

#######################################################"""
"""un/comment to de/activate ###########################

print(40 / 2) # 20.0
print(41 / 2) # 20.5

#######################################################"""
"""un/comment to de/activate ###########################

text = '''
Whose woods these are? I think I know.
His house is in the village though;
He will not see me stopping here
To watch his woods fill up with snow.

My little horse must think it queer
To stop without a farmhouse near
Between the woods and frozen lake
The darkest evening of the year.
'''

sentances_lst = text.split(".")
print(sentances_lst)

[
'Whose woods these are? I think I know',

' His house is in the village though; He will not see me stopping here To watch his woods fill up with snow',

' My little horse must think it queer To stop without a farmhouse near Between the woods and frozen lake The darkest evening of the year'
]
#######################################################"""
"""un/comment to de/activate ###########################

text = '''
Whose woods these are? I think I know.
His house is in the village though;
He will not see me stopping here
To watch his woods fill up with snow.

My little horse must think it queer
To stop without a farmhouse near
Between the woods and frozen lake
The darkest evening of the year.
'''

word_lst = text.split()
print(word_lst)
for word in text.split():
    print(word)

#######################################################"""
"""un/comment to de/activate ###########################

text = '''
Whose woods these are? I think I know.
His house is in the village though;
He will not see me stopping here
To watch his woods fill up with snow.

My little horse must think it queer
To stop without a farmhouse near
Between the woods and frozen lake
The darkest evening of the year.
'''
sentances = text.replace("?", ".").split(".")
print( sentances )
print( text )


#######################################################"""
"""un/comment to de/activate ###########################

text = '''
Whose woods these are? I think I know.
His house is in the village though;
He will not see me stopping here
To watch his woods fill up with snow.
'''

print( list(text) )


#######################################################"""
"""un/comment to de/activate ###########################

text = '''
Whose woods these are? I think I know.
His house is in the village though;
He will not see me stopping here
To watch his woods fill up with snow.
'''
words_lst    = text.split()
words_lst.append(500000000)
string_again =  " ".join( map(str, words_lst) )
print(string_again)


#######################################################"""
"""un/comment to de/activate ###########################

# lst = [33, 44, 22, 77, 55, 99, 55, 44, 88, 11, 22, 11]
# print(lst[3:6:])
text = '''
Whose woods these are? I think I know.
His house is in the village though;
He will not see me stopping here
To watch his woods fill up with snow.
'''
print(text[7:18:])


#######################################################"""
"""un/comment to de/activate ###########################

# lst = [22, 33, 55]
# print(33 in lst)

vowels = "aeiou"
c = "A"
print(c.lower() in vowels)

#######################################################"""
"""un/comment to de/activate ###########################

text = '''
Whose woods these are? I think I know.
'''
for idx, c in enumerate(text):
    print(idx, c)

#######################################################"""
"""un/comment to de/activate ###########################

text = '''whose woods these are? I think I know.'''
print(text)
print(text.lower())
print(text.upper())
print(text.capitalize())
print(text.swapcase())
print(text)


#######################################################"""
"""un/comment to de/activate ###########################

name = "Joanne"
age = 25
print( f"{name} is {age} years old" )

#######################################################"""
"""un/comment to de/activate ###########################

text = '''
Whose woods these are? I think I know.
His house is in the village though;
He will not see me stopping here
To watch his woods fill up with snow.
'''

print(text.count("."))
print(text.count("W"))
print(text.count("FFF"))
print(text.lower().count("his"))
print( len(text.split()) )

#######################################################"""
"""un/comment to de/activate ###########################

# CRUD
car = {
    "make"  : "toyota" ,
    "model" : "highlander" ,
    "year"  : 2014 ,
    }

# Read
print(car["year"])
# print(car["miles"]) # KeyError: 'miles'

# Create
car["miles"] = 100_00
print(car["miles"])

# Update
print(car["model"])
car["model"] = "huntsman"
print(car["model"])

# Delete
del car["miles"]
print(car)

#######################################################"""
"""un/comment to de/activate ###########################

# CRUD
car = {
    "make"  : "toyota" ,
    "model" : "highlander" ,
    "year"  : 2014 ,
    }


# for k, v in car.items():
#     print(v)

print("huntsman"   in car.values())
print("highlander" in car.values())

# a
print("miles"      in car.keys())
print("year"       in car.keys())
# b
print("miles"      in car) # same as car.keys()
print("year"       in car) # same as car.keys()

# a and b are EXACTLY the same

#######################################################"""
"""un/comment to de/activate ###########################

car = {
    "make"  : "toyota" ,
    "model" : "highlander" ,
    "year"  : 2014 ,
    }

# car["miles"]
print(  car.get( "miles", sorted() )  )

#######################################################"""
"""un/comment to de/activate ###########################

car = {}
car["make"]  = "toyota" ,
car["model"] = "highlander" ,
car["year"]  = 2014 ,

#######################################################"""
"""un/comment to de/activate ###########################

i = 0
while i < 10:
    i += 1
    print(i)

#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
