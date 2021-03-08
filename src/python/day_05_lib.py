"""un/comment to de/activate ###########################
# overview
# types
    # int float
    # bool
    # str
    # None
    # *tuple

    # list
    # *dict
    # *set

# functions
    # allow us encapsulate a process

# conditions
    # if elif else

# loops / iteration
    # repeat a body of code...


# recap
# functions
def factorial(n):
    prod = 1
    for i in range(2, n+1):
        prod *= i

    return prod

num = 4
# print( factorial( num ) )
# print( factorial( 5 ) )
# print( factorial( 37 ) )

# lists
    # mutable ordered collection of arbitrarry objects
    # range() # not a list
    # indexing

# range(5) # (0, 1, 2, 3, 4)
# range(3, 5) # (3, 4)
# range(3, 10, 3) # (3, 6, 9)


#######################################################"""
"""un/comment to de/activate ###########################
# list slicing -> gives back a section of the list

lst = [9, 8, 5, 7, 3, 3, 6, 7, 3, 6, 5, "last element"]
print( lst[10] )
print( lst[-3] )
# print( lst[12] ) # IndexError: list index out of range
# print( lst[-13] ) # IndexError: list index out of range



#######################################################"""
"""un/comment to de/activate ###########################

lst = [9, 8, 5, 7, 3, 3, 6, 7, 3, 6, 5]
print( lst[:4:]  ) # [9, 8, 5, 7] # beginning through idx 4 (EX)
print( lst[7::]  ) # [7, 3, 6, 5] # idx 7 through end of list
print( lst[::4]  ) # [9, 3, 3] # beginning in steps of 4
print( lst[::-1] ) # [5, 6, 3, 7, 6, 3, 3, 7, 5, 8, 9] reverse version of your list

print( lst[:20:] ) # no error, gives back entire list

# range(3, 10, 3)

#######################################################"""
"""un/comment to de/activate ###########################

lst = [[7, 5, "this thing here"], [3, 5, 1]]
print( lst[0][2][5:10:] )

#######################################################"""
"""un/comment to de/activate ###########################

# my_obj = "hello"
# print(id(my_obj)) # 140639038978352

lst = []
print(id(lst)) # 140387699391296
lst.append("hello")
print(id(lst)) # 140387699391296
lst.append("world")
print(id(lst)) # 140387699391296


my_string = ""
print(id(my_string)) # 140389830152944
my_string = my_string + "hello "
print(id(my_string)) # 140389888935536
my_string = my_string + "world"
print(id(my_string)) # 140389888936560

#######################################################"""
"""un/comment to de/activate ###########################

lst1 = [4, 3, 5]
# lst2 = lst1 # pointer duplication
lst2 = lst1.copy() # deep copy

lst2.append("hello")
print( lst2 ) # what's the value of lst2
print( lst1 ) # what's the value of lst1

#######################################################"""
"""un/comment to de/activate ###########################

fruit_lst = ["grapes", "blueberries", "apples"]
fruit_lst.append("bananas")
# ^^^ will cause -> ValueError: too many values to unpack (expected 3)
fruit1, fruit2, fruit3 = fruit_lst
print(fruit2)

#######################################################"""
"""un/comment to de/activate ###########################
# pass
def factorial(n):
    pass # placeholder


print("hi")

#######################################################"""
"""un/comment to de/activate ###########################
# loops: repeate processes
# for # where the number of iterations is known befor looping starts

lst = [3, 5, 4, "hello", 9.4, False]
num_lst = [] # target
sum_of_sqrs = 0 # target
for ele in lst:
    if type(ele) in [int, float]:
        num_lst.append(ele)
        sum_of_sqrs += ele**2

print(num_lst)


def factorial(n):
    prod = 1
    for i in range(2, n+1):
        prod *= i

    return prod


# while

#######################################################"""
"""un/comment to de/activate ###########################

lst = [4, 3, 5, 6, 7, 2]
print( sum(lst) )

#######################################################"""
"""un/comment to de/activate ###########################

def is_prime(num):
    prime = True
    if num < 2:
        prime = False

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    return prime

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


print(0, is_prime(0) ) # False
print(1, is_prime(1) ) # False
print(2, is_prime(2) ) # True
print(3, is_prime(3) ) # True
print(4, is_prime(4) ) # False
print(5, is_prime(5) ) # True
print(6, is_prime(6) ) # False
print(7, is_prime(7) ) # True
#######################################################"""
"""un/comment to de/activate ###########################

def is_divisible_by(num,divisor1,divisor2):
    if num%divisor1==0 and num%divisor2==0:
        print(f"This number is divisible by {divisor1} and {divisor2}.")
    elif num%divisor1==0:
        print(f"This number is divisible by {divisor1}.")
    elif num%divisor2==0:
        print(f"This number is divisible by {divisor2}.")
    else:
        print(f"This number is not divisible by either {divisor1} or {divisor2}.")



is_divisible_by(12, 3, 4) # This number is divisible by 3 and 4
is_divisible_by(12, 4, 5) # This number is divisible by 4
is_divisible_by(12, 5, 6) # This number is divisible by 6
is_divisible_by(12, 5, 7) # This number is not divisible by either 5 or 7


#######################################################"""
