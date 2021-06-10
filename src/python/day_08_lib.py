"""un/comment to de/activate ###########################

if condition:
    block

#######################################################"""
"""un/comment to de/activate ###########################

a = 0
if a < 10:
    print(a)


controller = 0
while controller < 10:
    controller += 1
    print(controller)


print( "fin" )

#######################################################"""
"""un/comment to de/activate ###########################

# is_prime(n) # bool # True if n is a prime number else False
def is_prime(n):
    if n < 2: return False

    for i in range(2, int(n**(1/2)) + 1 ):
        if n % i == 0:
            return False

    return True


# next_prime()
'''
next_prime

argument:
    n <list<int>>

return:
    <int> the next prime number after n
'''

# def next_prime(n):
#     while True: # loop forever
#         n += 1
#         if is_prime(n):
#             return n


# from itertools import count
# for i in count():
#     print(i)

# def next_prime(n):
#     while not is_prime(n+1):
#         n += 1
#
#     return n + 1
#
#
# for i in range(20):
#     print(i, next_prime(i))


#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
