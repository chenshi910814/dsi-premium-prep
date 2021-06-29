

def mean(lst, trim=0):
    lst_ = lst.copy()

    if trim > 0:
        lst_ = sorted(lst_)[trim:-trim]
    return sum(lst_) / len(lst_)

a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]

# print(mean(a, trim=2))


def variance(lst, sample=True):
    mean_ = mean(lst)
    total = 0.0

    for item in lst:
        total += (item - mean_)**2

    return total / (len(lst) - sample)

print(variance(a)**(1/2))