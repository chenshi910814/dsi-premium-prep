

a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]

def mean(lst, trim=0):
    lst_ = lst.copy()

    if trim > 0:
        lst_ = sorted(lst_)[trim:-trim]
    return sum(lst_) / len(lst_)

# print(mean(a, trim=2))




u = [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
f = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0, 0.3]

# # A
# print(f'Mean Urban: {round(mean(u), 1)}')
# print(f'Mean Farmhouse: {round(mean(f), 1)}')

# print()
# # B
# print(f'Mean Urban: {round(mean(u, 1), 1)}')
# print(f'Mean Farmhouse: {round(mean(f, 1), 1)}')



odd_list = [13, 18, 13, 14, 13, 16, 14, 21, 13]
even_list = [15, 14, 10, 8, 12, 8, 16, 13]


def median(lst):
    lst_sorted = sorted(lst)

    # odd
    if len(lst) % 2:
        mid = int(len(lst) / 2)
        return mid
print(odd_list)
print(median(odd_list))