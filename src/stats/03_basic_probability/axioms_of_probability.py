set1 = {'a', 'b', 'c'}
set2 = {'c', 'd', 'e'}

# commutative
print(set1.union(set2) == set2.union(set1))
print(set1.intersection(set2) == set2.intersection(set1))