"""un/comment to de/activate ###########################

a = 10
b = 10

print( a == b )
print( a != b )
print( a >  b )
print( a <  b )
print( a >= b )
print( a <= b )

#######################################################"""
# """un/comment to de/activate ###########################

# evaluation / execution
# data types
    # int, float
    # bool
    # str

# abstractions
    # variables

# controll flow
    # if, elif, else
# iteration

#######################################################"""
"""un/comment to de/activate ###########################

greeting = "Hello, "
name = "Clark"
cat_string = greeting + name
print( cat_string )

#######################################################"""
"""un/comment to de/activate ###########################

my_string = ""
my_string += "h"
my_string += "e"
my_string += "l"
my_string += "l"
my_string += "o"

print(my_string)

#######################################################"""
"""un/comment to de/activate ###########################

some_var = None
print( print("this is what I'm printing") )
# type()
# int()
# float()
# bool()
# str()


#######################################################"""
"""un/comment to de/activate ###########################

n = 12
m = 42
var = ((2 * n)**m)
print(var) # 9308338151941866618592771645958951941937449991757235224576

#######################################################"""
"""un/comment to de/activate ###########################

# x, y, z = 30, 40
# ValueError: not enough values to unpack (expected 3, got 2)
# x, y = 30, 40, 50
# ValueError: too many values to unpack (expected 2)

x, y, z = 30, 40, 20
print(x, y, z)
x = 30
y = 40
z = 20

#######################################################"""
"""un/comment to de/activate ###########################

print(True  and True)  # True
print(False and True)  # False
print(True  and False) # False
print(False and False) # False

print(True  or True)  # True
print(False or True)  # True
print(True  or False) # True
print(False or False) # False

print(not True)   # False
print(not False)  # True

print( not (True  and True) )  # False
print( not (False and True) )  # True
print( not (True  and False) ) # True
print( not (False and False) ) # True

print( not (True  or True) )  # False
print( not (False or True) )  # False
print( not (True  or False) ) # False
print( not (False or False) ) # True

print( not True  and True )  # False
print( not False and True )  # True
print( not True  and False ) # False
print( not False and False ) # False

#######################################################"""
"""un/comment to de/activate ###########################

(not (not (True or False) and (True and True))) and True or True

#######################################################"""
"""un/comment to de/activate ###########################

# ==
# !=
# >
# <
# >=
# <=

a = 3
b = 5

if a == b:
    print("a is equal to b")
elif a != b:
    print("a is not equal to b")
elif a > b:
    print("a is greater than b")
else:
    print("a is less than b")

# a is not equal to b
# a is less than b
print("fin")

#######################################################"""
"""un/comment to de/activate ###########################
'''
* Write a code snippet that checks two numbers, `x` and `y`:
    * Check if the sum of two numbers is greater than both numbers
        * If it is, print `"Both numbers are positive"`
    * Check if the sum is equal to either number
        * If it is, print `"At least one number is zero"`
    * Otherwise, print `"At least one number is negative"`
'''

def code_snippet(x, y):
    xy_sum = x + y
    if xy_sum > x and xy_sum > y:
        return "Both numbers are positive"
    elif xy_sum == x or xy_sum == y:
        return "At least one number is zero"
    else:
        return "At least one number is negative"

print(code_snippet(2, 3))
print(code_snippet(-2, 3))
print(code_snippet(2, -3))
print(code_snippet(-2, -3))
print(code_snippet(0, 3))
print(code_snippet(2, 0))
print(code_snippet(0, 0))
print(code_snippet(-2, 0))
print(code_snippet(0, -3))


#######################################################"""
"""un/comment to de/activate ###########################

x = int(input("input a value for x: "))
y = int(input("input a value for y: "))
if ((x + y) > x) and ((x + y) > y):
    print("Both numbers are positive")
elif ((x + y) == x) or ((x + y) == y):
    print("At least one number is zero")
else:
    print("At least one number is negative")

#######################################################"""
