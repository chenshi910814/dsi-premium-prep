# list/set trick for deduping

lst = ['kayaking', 'tennis', 'rolf ball', 'swimming', 'tennis', 'kayaking']

lst = list(set(lst))
print(lst) # --> ['swimming', 'tennis', 'kayaking', 'rolf ball']