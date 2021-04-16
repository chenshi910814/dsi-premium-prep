# """un/comment to de/activate ###########################

# overview
# evaluation / execution
    # expression -> code that gives back (expresses) a value
# data types
    # int, float
    # bool
        # ==, !=, >, <, >=, <=
    # str
    # None

    # list

# abstractions
    # variables
    # functions

# control flow
    # if, elif, else
    # if <condition>:
        # body

# iteration


#######################################################"""
"""un/comment to de/activate ###########################

if 7 > 5:
    print("hello")

#######################################################"""
"""un/comment to de/activate ###########################

def breakout_2( x ):
    if x % 2 == 0 and x % 5 == 0:
        return "Gimme 10!"
    elif x % 5 == 0:
        return "High Five!"
    elif x % 2 == 0:
        return "Evens!"
    else:
        return "I got nothing"


some_x = 9  # I got nothing
print(breakout_2(some_x))

some_x = 80 # Gimme 10!
print(breakout_2(some_x))

some_x = 25 # High Five!
print(breakout_2(some_x))

some_x = 66 # Evens!
print(breakout_2(some_x))

#######################################################"""
# """un/comment to de/activate ###########################

# IPO
# Inputs
# Process
# Output
# print()
    # Inputs
        # any type
    # Process
        # Writes it's inputs to the console
    # Output
        # None

# type()
    # Inputs
        # any type
    # Process
    # Output
        # type of the input


# len()
    # Inputs
        # any iterable type
            # str
            # list
    # Process
    # Output
        # int: representing the length of the input



#######################################################"""
"""un/comment to de/activate ###########################

# definition
def factorial( n ):
    prod = 1
    for i in range(1, n+1):
        prod *= i

    return prod


# invocation/call
result = factorial(7)
print(result)


# factorial
    # I
        # int
        # NOTE: can't be a float onaly an int
    # P
    # O
        # int:
            # represents the factorial of the int passed in as an argument

#######################################################"""
"""un/comment to de/activate ###########################

# def decrement(m=1, n):
    # SyntaxError: non-default argument follows default argument

def decrement(n, m=1):
    return n - m

my_number = 53
dec = 30
print( decrement(my_number, dec) )
# TypeError: decrement() missing 1 required positional argument: 'm'


#######################################################"""
"""un/comment to de/activate ###########################

def some_func(x):
    print(x) # 10


print( some_func(10) ) # None


def some_other_func(x):
    return x


print( some_other_func(10) ) # 10

#######################################################"""
"""un/comment to de/activate ###########################

# WARNGING!!!

y = 15
def my_function(x, y):
    return x * y

y = 0 # mistake
print(my_function(3, y))

print(my_function(3, 30))
print(my_function(3, 4))

#######################################################"""
"""un/comment to de/activate ###########################

# state = "Alaska"
# print( f'{state} is one of the states in the US' )

name = "Sally"
age = 47
print( f"{name} is {age} years old" )

#######################################################"""
# """un/comment to de/activate ###########################




#######################################################"""
