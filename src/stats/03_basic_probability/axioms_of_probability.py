
'''
Commutative
A ∪ B = B ∪ A
AB = BA
'''
set1 = {'a', 'b', 'c'}
set2 = {'c', 'd', 'e'}

# print(set1.union(set2) == set2.union(set1))
# print(set1.intersection(set2) == set2.intersection(set1))

a = True
b = False

# print( (a or b) == (b or a))
# print( (a and b) == (b and a))


'''
Associative
'''
set1 = {'a', 'b', 'c'}
set2 = {'c', 'd', 'e'}
set3 = {'a', 'e', 'f'}

# print( (set1.union(set2)).union(set3) == (set3.union(set2)).union(set1) ) # --> True
# print( (set1.intersection(set2)).intersection(set3) == (set3.intersection(set2)).intersection(set1)) # --> True


