"""un/comment to de/activate ###########################

# python overview
# data types
    # int, float
    # bool
    # None
    # str

    # list
        # discribe mutability vs immutability

# abstractions
    # variables
    # functions

# control flow
    # if, elif, else

# iteration
    # for
    # while

###################################################### """
"""un/comment to de/activate ###########################

txt = "hello"
print(txt)

txt = txt + " world"
print(txt)

###################################################### """
"""un/comment to de/activate ###########################

'''
* Write a function that computes and returns a list of all of the divisors of some positive number. Use a while loop. Things to think about:
    * How do you determine if a single number is a divisor of another?
    * What is your stopping condition?
    * BONUS: rewrite this with a for loop

IPO (input, process, output):

input:
    n <int>: a positive integer

output:
    <list <int> >: representing all the divisors of n
'''

def divisors_list(n):
    lst = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst.append(i)

    return lst


def divisors_list(n):
    lst = []
    i = 0
    while i <= n:
        i += 1
        if n % i == 0:
            lst.append(i)

    return lst


for i in range(20):
    print( i, divisors_list(i) )

###################################################### """
"""un/comment to de/activate ###########################

lst = []
while True: # loop forever
    menu_string = '''Select from this list:
    1 : bread
    2 : butter
    3 : potatoes
    4 : broccoli
    q to quit'''
    print(menu_string)
    inp = input("please make a selection 1-4: ")
    if inp.lower() == "q": break
    lst.append( int(inp) )

print(lst)

###################################################### """
"""un/comment to de/activate ###########################

txt = '''
hello
world
'''

txt = 'that\'s'
print(txt)

###################################################### """
"""un/comment to de/activate ###########################

txt = "hello "
print( txt + "world" )
print( txt * 3 )
print( txt )

###################################################### """
"""un/comment to de/activate ###########################

a = 10
print(a)
a = str(a)
print(a)

b = 3.5
print(b)
print(str(b))

c = [4, 5, 2]
print(c)
print(str(c))

d = None
print(d)
print(str(d))

e = True
print(e)
print(str(e))

f = False
print(f)
print(str(f))

###################################################### """
"""un/comment to de/activate ###########################

a = "10"
print(a)

b = float(a)
print(b)

###################################################### """
"""un/comment to de/activate ###########################

print( bool("hello") ) # True
print( bool("") )      # False

###################################################### """
"""un/comment to de/activate ###########################

text = '''
Whose woods these are I think I know
His house is in the village though
He will not see me stopping here
To watch his woods fill up with snow
'''

world_lst = []
word = ""
for el in text:
    if el == " ":
        world_lst.append(word)
        word = ""
    else:
        word += el


print(world_lst)
print(text.split())

###################################################### """
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

He gives his harness bells a shake
To ask if there is some mistake.
The only other sound's the sweep
Of easy wind and downy flake.

The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep.
'''

# print( list(text) )
# print(text.split())
# for word in text.split():
#     print(word)
#
# print(text.split("."))
# for sentance in text.split("."):
#     print(sentance)

sentances_lst = text.split(".")
print(sentances_lst)

print( " ".join(sentances_lst) )

###################################################### """
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

He gives his harness bells a shake
To ask if there is some mistake.
The only other sound's the sweep
Of easy wind and downy flake.

The woods are lovely, dark and deep,
But I have promises to keep,
And miles to go before I sleep,
And miles to go before I sleep.
'''

print( text[7:22:] )

###################################################### """
"""un/comment to de/activate ###########################

lst = [5, 4, 3, 2, 1]
print(6 in lst)
print(2 in lst)

txt = "hello world"
print("o" in txt)
print("p" in txt)
print("ello" in txt)

###################################################### """
"""un/comment to de/activate ###########################

lst = [5, 4, 3, 2, 1]
txt = "hello world"

# for ch in txt:
#     print(ch)

for idx, ele in enumerate(txt):
    print(idx, ele)

###################################################### """
"""un/comment to de/activate ###########################

lst = [4, 3, 5, 0, 1]
# 4351
# print(  list( map(bool, lst) )  )

def my_map(fn, lst):
    acc = []
    for ele in lst:
        acc.append(fn(ele))

    return acc


digits = "".join( my_map(str, lst) )
print(digits)

###################################################### """
# """un/comment to de/activate ###########################



###################################################### """
