"""un/comment to de/activate ###########################

# len
# Input
    # some collection ie a list or string or tuple
# Process
# Output
    # int representing the lenght of the input

lst = [ 44, 33, 55, 44]
# list
# append
# pop
# len
    # len(lst)
# sum
# sorted
# max
# min
# count
    # lst.count(44)
# index

# enumerate
# zip

for idx, ele in enumerate(lst): pass
for a, b in zip(lst_a, lst_b): pass


#######################################################"""
"""un/comment to de/activate ###########################

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int( n**(1/2) ) + 1):
        if n % i == 0:
            return False

    return True


def next_prime(n):
    while not is_prime(n + 1):
        n += 1

    return n + 1


for i in range(20):
    print( i, next_prime(i) )


for _ in range(10_000_000):
    print(_)

#######################################################"""
"""un/comment to de/activate ###########################
'''
Write a function that computes and returns a list of all of the divisors of some positive number.

Use a while loop. Things to think about:
How do you determine if a single number is a divisor of another?

What is your stopping condition?

BONUS: rewrite this with a for loop
'''

def factors_lst(n):
    lst = []
    i = 0
    while True:
        i += 1
        if n % i == 0: lst.append(i)
        if i >= n: break

    return lst


print( factors_lst(24) )


#######################################################"""
"""un/comment to de/activate ###########################

selections = []
make_order = True

while make_order:
    print('''Select from this list:
    1 : bread
    2 : butter
    3 : potatoes
    4 : broccoli''')

    inp = int(input('please make a selection, 1-4: '))

    if inp in [1,2,3,4]:
        selections.append(inp)
    else:
        print('-- your selection was not understood --')
        continue

    inp2 = input('would you like to place another order? (y/n)')

    if inp2 == 'y':
        continue
    else:
        make_order = False


print(f'Your order list: {selections}')



#######################################################"""
"""un/comment to de/activate ###########################

''
""

'''
'''

# 235

# CSI
my_string = "hello"
# print( my_string )
my_string += " world"
# my_string = my_string + " world"
# print( my_string )

# print( my_string[4:9:] )
# print( my_string * 3 )

# membership
# print( "z" in my_string )

# case transforms
# res = my_string.upper() # "HELLO WORLD"
# print( my_string.upper() ) # hello world
# print( my_string ) # hello world

# my_string = "hello. world"
# print( my_string.capitalize() )

my_string = "HELlO WoRlD"
# print( my_string.lower() )


# my_string = "something"

# count
# print(my_string.lower().count("l"))

# replace
# my_string = "hello world"
# res = my_string.replace("lo w", "<HEY>")
# print( res )

# casting
# print( [str([8, 7,2     ,3])] )

# methods # dir

# list / split / join
# my_string = "hello. world"
# print( list(my_string) )
# splt_string = my_string.split()

text = '''
Whose woods these are? I think I know.
His house is in the village though;
He will not see me stopping here
To watch his woods fill up with snow.
'''

# for sentance in text.replace("?", ".").replace(";", ".").split("."):
#     print(sentance)

words_lst = text.split()
words_lst.append(57)
words_str = " ".join( map(str, words_lst) )
# TypeError: sequence item 30: expected str instance, int found

print(words_str)

# enumerate


#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
