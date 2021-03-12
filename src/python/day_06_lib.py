# """un/comment to de/activate ###########################

# types
    # int, float
    # bool
    # str
    # None

    # list

# functions
    # return will stop the function

# conditions
    # run code only when some condition is True

# loops
    # repeate a process


#######################################################"""
"""un/comment to de/activate ###########################

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


for i in range(15):
    print( i, is_prime(i) )


#######################################################"""
"""un/comment to de/activate ###########################

for i in range(5):
    if i < 2:
        continue # skip to the next iteration of the loop
    print(i)

#######################################################"""
"""un/comment to de/activate ###########################

def is_prime(n):
    pass


def next_prime(n):
    pass

#######################################################"""
"""un/comment to de/activate ###########################

lst = []
lst.append("hello")
lst.append("hello")
lst.append("hello")
lst.append("hello")
print( lst )

#######################################################"""
"""un/comment to de/activate ###########################

# print( dir([]) )

# append
# clear
# lst = [99, 33, 44]
# lst.clear()
# print(lst)

# copy
# lst = []
# print( id(lst), lst )
# lst.append(10)
# print( id(lst), lst )

# count
# lst = [99, 33, 44, 33]
# print(lst.count(33))
# print(lst.count(99))
# print(lst.count(77))

# extend
# lst = [99, 33, 44, 33]
# lst.extend( ["hello", "world"] )
# print(lst)

# index
# lst = [99, 33, 44, 33]
# print( lst.index(33) ) # 1

# insert
# lst = [99, 33, 44, 33]
# lst.insert(3, "hello")
# print(lst)

# pop
# lst1 = [99, 33, 44, 33]
# lst2 = lst1.copy()
# print(lst2.pop(2))
# print(lst1)
# print(lst2)

# remove
# lst = [99, 33, 44, 33]
# lst.remove(33)
# print(lst)

# lst = [ 99, 33, 44, 33 ]
# print( len(lst) )
# print( sum(lst) )

# print( sum([99, 33, 44, 33, "hello"]) )
# ^^^ TypeError: unsupported operand type(s) for +: 'int' and 'str'

# print(range(10)) # range(0, 10)
# print(  sum( range(3, 17) )  )

#######################################################"""
"""un/comment to de/activate ###########################
# my_lib
def example(lst, obj):
    lst = lst.copy()
    lst.append(obj)
    return lst


###############################################
my_lst = ["hello", "world"]
print( example(my_lst, "hi") )
print( my_lst )

#######################################################"""
"""un/comment to de/activate ###########################

lst = [44, 77, 22, 99, 33, 11]
for i in sorted(lst, reverse=False):
    print(i)

# print( reversed(lst) )
# print( lst )

#######################################################"""
"""un/comment to de/activate ###########################

lst = [44, 77, 22, 99, 33, 11]
print( min(lst) )
print( max(lst) )

#######################################################"""
"""un/comment to de/activate ###########################

lst = ["", [], (), 0, 0.0]
print(  any(lst)  )

lst = [44, 77, 22, 99, 33, 11]
print(  all(lst)  )

#######################################################"""
"""un/comment to de/activate ###########################

lst = [44, 77, 22, 99, 33, 11]
for idx, num in enumerate(lst):
    print(num**idx)

#######################################################"""
"""un/comment to de/activate ###########################

names = ["Jane", "Joe", "Jessie"]
ages  = [32    , 57   , 98]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

#######################################################"""
"""un/comment to de/activate ###########################

# for loops
# while loops # conditional loops
# conditions

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# def next_prime(n):
#     while not is_prime(n+1):
#         n += 1
#     return n + 1


def next_prime(n):
    while True: # loop forever
        n += 1
        if is_prime(n):
            return n


for i in range(15):
    print( i, next_prime(i) )

#######################################################"""
"""un/comment to de/activate ###########################

i = 0
while i < 1_000_000:
    i += 1
    if i > 1_000: break
    print(i)


# for _ in range(10_000_000):
#     if condition_met:
#         break


#######################################################"""
"""un/comment to de/activate ###########################

lst = []
while True:
    lst.append( input("enter a name: ") )
    if input("do you want to enter another name? Y or N: ") == "N":
        break

#######################################################"""
"""un/comment to de/activate ###########################

lst = [44, 77, 22, 99, 33, 11]
print( id(lst) )
print( id(lst[::]) )
print( id(lst) )

#######################################################"""
"""un/comment to de/activate ###########################
def example(lst1, obj):
    lst2 = lst1.copy()
    lst2.append(obj)
    return lst2


###############################################
my_lst = ["hello", "world"]
print( example(my_lst, "hi") )
print( my_lst )


#######################################################"""
"""un/comment to de/activate ###########################

lst = [44, 77, 22, 99, 33, 11]
sorted_lst = sorted(lst)
print(id(lst), lst)
print(id(sorted_lst), sorted_lst)

#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
