# list/set trick 
lst = ['skiing', 'shuffleball', 'swimming', 'swimming', 'golf']

# print(list(set(lst)))


def dedupe_in_order(lst):
    deduped = []

    for element in lst:
        if element not in deduped:
            deduped.append(element)
    return deduped

# print(dedupe_in_order(lst))


a = ['bat', 'cat', 'dog', 'porpoise', 'whale', 'ant', 'bear']
b = ['bat', 'cat', 'dog', 'eagle', 'shark', 'anteater', 'gull']
c = ['porpoise', 'platypus', 'crane', 'hermit crab', 'shark', 'anteater', 'gull']


def union(set1, set2):
    set_union = set1.copy()

    for item in set2:
        if item not in set_union:
            set_union.append(item)
    return set_union

print(union(union(a, b), c)) # -> all unique elems from a and b