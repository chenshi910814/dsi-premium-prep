

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



