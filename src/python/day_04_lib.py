# """un/comment to de/activate ###########################

# types
    # int float
        # int(), float(), + - * / // % **
    # bool
    # str
    # lists

# functions
    # containers for the code

# conditions
    # if elif else
    # if condition:
        # body

# loops
    # "iterate" aka repeat processes


#######################################################"""
"""un/comment to de/activate ###########################

# print( 0.999999999999999999999 )
# 1.0

#######################################################"""
"""un/comment to de/activate ###########################

3 == 3

print() # only for writing to the console

#######################################################"""
"""un/comment to de/activate ###########################

# IPO
# print()
# int()
    # print( int("hello") ) # ValueError: invalid literal for int() with base 10: 'hello'


def factorial(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i

    return prod


num = 4
print( factorial(4) )
print( factorial(num) )
print( factorial(num + 1) )

#######################################################"""
"""un/comment to de/activate ###########################

# identifier and a value

# definition #####################################
# a and b are called parameters
# inputs DON'T have values here
# parameters are generic
def add_nums(a, b):
    return a + b # output

# envocation #####################################
# the inputs are called arguments
# inputs DO have values here
# arguments are specific
this_a = 10
this_b = 20
print( add_nums(this_a, this_b) ) # 30
print( add_nums(30 / 2, 12) ) # 27.0
print( add_nums(3, 12) ) # 15

import math
print( add_nums(math.e, math.pi) ) # 5.859874482048838


# print( 30 + 12 ) # 42

30
27.0
15
42

30
None
27.0
None
15
None
#######################################################"""
"""un/comment to de/activate ###########################

def add_10(num, b=10):
    return a + b

############################################
print( add_10(2) )
print( add_10(2, 100) )
print( add_10() )

#######################################################"""
"""un/comment to de/activate ###########################

# "represent bodies of text"
name = "Billy"
age = 7
print( f"{name} is {age} years old" )
print( name + " is " + str(age) + " years old" )

#######################################################"""
"""un/comment to de/activate ###########################

name = input("Please enter your name: ")
half_age = input("Please enter half your age: ")
age = int(half_age) * 2
print( f"{name} is {age} years old" )

#######################################################"""
"""un/comment to de/activate ###########################

a = 1000
def add_10( b ):
    a = 10
    return a + b


print( add_10( a ) )
print( a )

#######################################################"""
"""un/comment to de/activate ###########################

# my_list = [4, 6.4, "hello", 9, "world", 9, 4, 7, ["hey", "i'm a list"]]

# my_list = [4, 3, 5]
my_list = []
print( my_list )

#######################################################"""
"""un/comment to de/activate ###########################
# range(start, stop, step)

# range(stop)
range( 5 ) # 0, 1, 2, 3, 4

# range(start, stop)
range( 7, 10 ) # 7, 8, 9
n = 10
range( 7, n+1 ) # 7, 8, 9, 10

# range(start, stop, step)
range( 7, 15, 2 ) # 7, 9, 11, 13

#######################################################"""
"""un/comment to de/activate ###########################

# print( type(range(4, 10)) )

my_lst = [55, 77, 33, "hi", 44]
print( my_lst[3] ) # "hi"


#######################################################"""
"""un/comment to de/activate ###########################

# bool
print( 7 in [2, 3, 5, 7, 11] )
# print( 7 == 2 or 7 == 3 or 7 == 5 or 7 == 7 or 7 == 11 )

#######################################################"""
# """un/comment to de/activate ###########################

# print(f"{hello}")

#######################################################"""
"""un/comment to de/activate ###########################

'''
Write a function that uses the input() function inside of it to take a user inputted number and check if that number is equal to 7. If the number is equal to 7, return True. If not, return False
Hint: input() will return a string by default, so cast to an int:
user_input = int(input('type number: '))
'''

# "no output" /-> writes to console
def is_this_equal_to_7():
    user_input = int(input('type a number: '))
    if user_input == 7:
        print(True)
    else:
        print(False)


# output
def is_this_equal_to_7():
    user_input = int(input('type a number: '))
    if user_input == 7:
        return True
    else:
        return False

print( is_this_equal_to_7() )

#######################################################"""
"""un/comment to de/activate ###########################

def add_10( b ):
    a = 10
    # return a + b
    print(a, b)


a = 40
print( add_10( a ) ) # None



#######################################################"""
