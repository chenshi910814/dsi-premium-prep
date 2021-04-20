# """un/comment to de/activate ###########################

# types
    # immutable
        # int, float
        # bool
            # == != < > <= >=
            # in
        # str
        # None

    # mutable
        # list

# abstractions
    # var
    # functions
        # 2phases
        # def
        # invoke

# control flow
    # if, elif, else
    # bool

# iteration
    # for loops

#######################################################"""
"""un/comment to de/activate ###########################

ages_lst = [34, 58, 77, 29, 21, 31, 41, 55]
# print( ages_lst[-9] ) # IndexError: list index out of range
# print( ages_lst[8] ) # IndexError: list index out of range
print(ages_lst)


#######################################################"""
"""un/comment to de/activate ###########################

n = 102
my_range = list(range(3, n+1, 9))
print(my_range)

#######################################################"""
"""un/comment to de/activate ###########################

ages_lst = [34, 58, 77, 29, 21, 31, 41, 55]

# print(55 in ages_lst)
n = 5
print( ages_lst[2:n+1:] )


#######################################################"""
"""un/comment to de/activate ###########################

lst_o_lsts = [[11, 22, 33], [44, 55], [66, 77, 88, 99]]
print( lst_o_lsts[2][1] )

#######################################################"""
"""un/comment to de/activate ###########################

lst = []
print( id(lst), lst )

lst.append( "hello" )
print( id(lst), lst )

########################
string = ""
print( id(string), string )

string = string + "hello "
# string = string + "world"

print( id(string), string )

# my_car.color("black")
# my_car.color("red")

#######################################################"""
"""un/comment to de/activate ###########################

lst1 = ["a", "b", "c"]
lst2 = lst1.copy() # copy
lst2.append("d")
print(lst2)
print(lst1)

#######################################################"""
"""un/comment to de/activate ###########################

ages_lst = [34, 58, 77, 29, 21, 31, 41, 55]

ages_count = 0
ages_sum = 0
for age in ages_lst:
    ages_count += 1
    ages_sum += age

print(ages_sum / ages_count)

mean_age = sum(ages_lst) / len(ages_lst)

#######################################################"""
"""un/comment to de/activate ###########################

ages_lst = [34, 58, 77, 29, 21, 31, 41, 55]

ages_sum = 0
for age in ages_lst:
    ages_sum += age

print(ages_sum)

# mean_age = sum(ages_lst) / len(ages_lst)
# print(mean_age)

#######################################################"""
"""un/comment to de/activate ###########################

for identifier in iterable:
    body
    of
    code


#######################################################"""
"""un/comment to de/activate ###########################

lst = [34, 58, 77, 29, 21, 31, 41, 55]

sqrs_lst = []
for ele in lst:
    sqrs_lst.append(ele**2)


print(sqrs_lst) # [1156, 3364, 5929, 841, 441, 961, 1681, 3025]

#######################################################"""
"""un/comment to de/activate ###########################

lst = [34, 58, 77, 29, 21, 31, 41, 55]
tally = 0
sum_greater_than_100 = False
for num in lst:
    tally += num
    if tally > 100:
        sum_greater_than_100 = True
        print(tally)
        break

if sum_greater_than_100:
    print("the sum was greater than 100")

#######################################################"""
"""un/comment to de/activate ###########################

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


for i in range(20):
    print( i, is_prime(i) )


#######################################################"""
"""un/comment to de/activate ###########################

ages_lst = [34, 58, 77, 29, 21, 31, 41, 55]

ages_sum = 0
snapper_lst = []
for age in ages_lst:
    if age < 40:
        snapper_lst.append(age)

print(snapper_lst)

# mean_age = sum(ages_lst) / len(ages_lst)
# print(mean_age)


#######################################################"""
"""un/comment to de/activate ###########################

# mutable
    # val can change w/o changin id
# collection of arbitrary elements
# iterate through with a for loop
# auto assaigned index for each element


#######################################################"""
