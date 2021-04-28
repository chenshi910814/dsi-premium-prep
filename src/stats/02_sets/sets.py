# list/set trick for deduping

lst = ['kayaking', 'tennis', 'rolf ball', 'swimming', 'tennis', 'kayaking']


# print(list(set(lst))) # --> ['swimming', 'tennis', 'kayaking', 'rolf ball']


def dedupe_in_order(lst):
    deduped = []

    for element in lst:
        if element not in deduped:
            deduped.append(element)
    
    return deduped

print(dedupe_in_order(lst))