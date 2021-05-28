"""un/comment to de/activate ###########################

# types
    # int, float
    # bool
        # < > <= >= == !=
        # not, and, or
    # str
    # None

# abstractsions
    # variables
    # functions
    # classes

# control flow
    # if, elif, else
    # if <condition>: <consequent>

# iteration
    # for
    # while

#######################################################"""
"""un/comment to de/activate ###########################

a = 5
b = 5
if   a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")


print("program finished")

#######################################################"""
"""un/comment to de/activate ###########################

def factorial(n):
    prod = 1
    for i in range(2, n+1):
        prod *= i

    return prod


print( factorial(5) )

#######################################################"""
"""un/comment to de/activate ###########################

# IPO
# input   : any 2 numbers, either int or float
# porcess : subtract the second from the first
# output  : <int> or <float> the difference between the first and second input

def subtract(a, b):
    difference = a - b
    return difference

print( subtract(5, 2) )

#######################################################"""
"""un/comment to de/activate ###########################

print(0.9)
print(0.99)
print(0.999)
print(0.9999)
print(0.99999)
print(0.999999)
print(0.9999999)
print(0.99999999)
print(0.999999999)
print(0.9999999999)
print(0.99999999999)
print(0.999999999999)
print(0.9999999999999)
print(0.99999999999999)
print(0.999999999999999)
print(0.9999999999999999)
print(0.99999999999999999)
print(0.999999999999999999)
print(0.9999999999999999999)
print(0.99999999999999999999)
print(0.999999999999999999999)
# print(1/100**100000)

#######################################################"""
"""un/comment to de/activate ###########################

def subtract(a, b):
    difference = a - b
    return difference


print( subtract(5, 2) + 3 )



def subtract(a, b):
    difference = a - b
    print(difference)


print( subtract(5, 2) )


#######################################################"""
"""un/comment to de/activate ###########################

# def subtract(a=10, b):
# SyntaxError: non-default argument follows default argument
def subtract(a, b):
    difference = a - b
    return difference


print( subtract(7, 3) )
# print( subtract(a=7, b=3) )
# TypeError: subtract() missing 1 required positional argument: 'b'

#######################################################"""
"""un/comment to de/activate ###########################

name = "Joanne"
age  = 38
print( "{} is {} years old".format(name, age) )

#######################################################"""
"""un/comment to de/activate ###########################


def some_unknown_number(a, b):
    difference = a - b
    return difference


x = 10
y = 30
print( some_unknown_number(x, y) )

#######################################################"""
"""un/comment to de/activate ###########################

def user_info(username, email, age):
    return f"{username} is {age} years old, their email is {email}"


print(user_info("clark", "clarks_real_email@emailprovider.com", 97))

#######################################################"""
"""un/comment to de/activate ###########################
'''
Implement the function dbl_seq_sum which takes two lists of positive integers and computes the summation

Where a[k] and b[k] refer to the k-th elements in the two given lists. Notice that there is no upper bound on the summation. This just means "sum over all the elements". Assume that both lists will be the same length, and take note of the starting index of the summation.
'''

def dbl_seq_sum(nums_a, nums_b):
    summation = 0
    for idx, numa in enumerate(nums_a, 1):
        summation += ((-1)**idx) * ((numa + nums_b[idx-1]) / ((1 + numa * nums_b[idx-1] )))

    return summation


print( dbl_seq_sum([3, 5, 2], [7, 1, 9]) )

def dbl_seq_sum(nums_a, nums_b):
    acc = 0
    for k, (a, b) in enumerate(zip(nums_a, nums_b), 1):
        acc += ((-1)**k) * ((a + b) / (1 + (a * b)))

    return acc


print( dbl_seq_sum([3, 5, 2], [7, 1, 9]) ) #

#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
