# list/set trick for deduping

lst = ['kayaking', 'tennis', 'rolf ball', 'swimming', 'tennis', 'kayaking']


# print(list(set(lst))) # --> ['swimming', 'tennis', 'kayaking', 'rolf ball']


def dedupe_in_order(lst):
    deduped = []

    for element in lst:
        if element not in deduped:
            deduped.append(element)
    
    return deduped

# print(dedupe_in_order(lst))



# STAR ARGS:  *args

def prod_nums(*nums):
    prod = 1
    for num in nums:
        prod *= num
    return prod

# print(prod_nums(5,3,5,7,6,9,5,8,1,3,5,7))
# print(prod_nums(5,3,5,))








anim_1 = ['jellyfish', 'lion', 'tiger', 'cricket', 'squid', 'cat'] 
anim_2 = ['tiger', 'cat', 'eagle', 'shark', 'manta ray']
anim_3 = ['lion', 'tiger', 'meerkat', 'dog', 'shark', 'eagle', 'prairie dog']

def union(lst1, lst2):
    set_union = lst1.copy()

    for item in lst2:
        if item not in set_union:
            set_union.append(item)
    
    return set_union

# print(union(anim_1, anim_2)) # ['jellyfish', 'lion', 'tiger', 'cricket', 'squid', 'cat', 'eagle', 'shark', 'manta ray']


def union_mult_sets(*mult_sets):
    set_union = []

    for lst in mult_sets:
        for item in lst:
            if item not in set_union:
                set_union.append(item)
    
    return set_union

# print(union_mult_sets(anim_1, anim_2, anim_3))


anim_1 = ['jellyfish', 'lion', 'tiger', 'cricket', 'squid', 'cat'] 
anim_2 = ['tiger', 'cat', 'eagle', 'shark', 'manta ray']
anim_3 = ['lion', 'meerkat', 'dog', 'shark', 'eagle', 'prairie dog', 'tiger']

def intersection(lst1, lst2):
    set_intersect = []

    for item in lst1:
        if item in lst2:
            set_intersect.append(item)
    return set_intersect

# print(intersection(anim_1, anim_2)) # ['tiger', 'cat']


def intersection_mult_sets(*mult_sets):
    set_intersect = []

    # make sure we have more than one set and each set has more than 0 elements
    if len(mult_sets) > 1 and all([len(lst)>0 for lst in mult_sets]):
        for item in mult_sets[0]:
            is_member = True

            for set_ in mult_sets[1:]:
                if item not in set_:
                    is_member = False
                    break
            if is_member:
                set_intersect.append(item)
    return set_intersect

# print(intersection_mult_sets(anim_1, anim_2, anim_3))


def difference(lst1, lst2):
    set_difference = lst1.copy()

    for item in lst1:
        if item in lst2:
            set_difference.remove(item)
    return set_difference

# print(difference(anim_1, anim_2)) # ['jellyfish', 'lion', 'cricket', 'squid'] 

sample_space = union_mult_sets(anim_1, 
                               anim_2, 
                               anim_3, 
                               ['snake', 'whale', 'bat', 'cat']
                               )

def complement(sample_space, lst1):
