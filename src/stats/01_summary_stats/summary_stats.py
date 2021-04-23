

a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]

def mean(lst, trim=0):
    lst_ = lst.copy()

    if trim > 0:
        lst_ = sorted(lst_)[trim:-trim]
    return sum(lst_) / len(lst_)

print(mean(a, trim=2))