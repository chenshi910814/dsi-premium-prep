# sets have unique objects
lst = ['chair', 'table', 'stove', 'table']

lst_dupes_rmvd = list(set(lst))

# print(lst_dupes_rmvd) # ['table', 'stove', 'chair']



def dedupe_in_order(lst):
    deduped = []

    for element in lst:
        if element not in deduped:
            deduped.append(element)
    return deduped

lst = ['chair', 'table', 'stove', 'table']
# print(dedupe_in_order(lst))



'''
Union Function
'''
A = ['bat', 'cat', 'dog', 'weasel', 'dolphin', 'zebra']
B = ['dog', 'weasel', 'dolphin', 'zebra', 'squirrel', 'vole']
C = ['dolphin', 'zebra', 'squirrel', 'vole', 'manatee', 'sloth']

def union(lst1, lst2):
    set_union = lst1.copy()

    for item in lst2:
        if item not in set_union:
            set_union.append(item)

    return set_union


# print(union(A, B))
# print(union(B, C))


'''
*args
'''

# def star_args(*args):
#     print(type(args))
#     for item in args:
#         print(item)
#     return None
    
# star_args([1,2,3,4,5,6], 'cat', 32.7)


def union_mult_sets(*mult_sets):
    set_union = mult_sets[0]

    if len(mult_sets) > 1:
        for next_set in mult_sets[1:]:
            set_union = union(set_union, next_set)

    return set_union
    
    # for lst in mult_sets:
    #     for item in lst:
    #         if item not in set_union:
    #             set_union.append(item)
    # return set_union

# print(union_mult_sets(A, B, C))


'''
intersection
'''

def intersection(lst1, lst2):
    set_intersect = []

    for item in lst1:
        if item not in set_intersect:
            if item in lst2:
                set_intersect.append(item)

    return set_intersect

# A_and_B = intersection(A, B)
# print(A_and_B)
# print(intersection(A_and_B, C))


def intersection_mult(*mult_sets):
    set_intersect = []

    if len(mult_sets) > 1 and len(mult_sets[0]) > 0:
        for item in mult_sets[0]:
            is_member = True

            for set_ in mult_sets[1:]:
                if item not in set_:
                    is_member = False
                    break

            if is_member:
                set_intersect.append(item)
    
    return set_intersect
        

# print(intersection_mult(A, B, C))



'''
Set Difference
'''

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# A - B => {1, 2}
# B - A => {5, 6}

def difference(lst1, lst2):
    set_difference = []

    for item in lst1:
        if item not in lst2:
            set_difference.append(item)
    return set_difference


A = ['bat', 'cat', 'dog', 'weasel', 'dolphin', 'zebra']
B = ['dog', 'weasel', 'dolphin', 'zebra', 'squirrel', 'vole']
C = ['dolphin', 'zebra', 'squirrel', 'vole', 'manatee', 'sloth']

# print(difference(A, B))
# print(difference(B, A))



'''
Complement
'''

D = {'eel', 'baskeball'}

sample_space = union_mult_sets(A, B, C, D)


difference(sample_space, lst):
