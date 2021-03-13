def mean(lst, trim=0):
    lst_ = lst.copy()

    if trim > 0:
        lst_ = sorted(lst_)[trim:-trim]

    return sum(lst_) / len(lst_)

a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]

# print(mean(a)) # 238.3
# print(mean(a, trim=1)) # 47.75
# print(mean(a, trim=2)) # 26.16


'''
An article published in the journal, Indoor Air, considered two different air samples to test for endotoxin concentrations, the first in urban households, and the second in farmhouses.
'''

urban =  [6.0, 5.0, 11.0, 33.0, 4.0, 5.0, 80.0, 18.0, 35.0, 17.0, 23.0]
farmhouse = [4.0, 14.0, 11.0, 9.0, 9.0, 8.0, 4.0, 20.0, 5.0, 8.9, 21.0, 9.2, 3.0, 2.0, 0.3]

# A. Determine the sample mean for each group.

# print(f'Mean Urban: {round(mean(urban), 1)}')
# print(f'Mean Farmhouse: {round(mean(farmhouse), 1)}')


# B. Determine the trimmed mean for each group by trimming the smallest and largest value from each group.
# print(f'Trimmed Mean Urban: {round(mean(urban, trim=1), 1)}')
# print(f'Trimmed Mean Farmhouse: {round(mean(farmhouse, trim=1), 1)}')



def median(lst):
    lst_sorted = sorted(lst)

    # if odd
    if len(lst) % 2 == 1:
        mid = int(len(lst) / 2)
        return lst_sorted[mid]
    else:
        upper_mid = int(len(lst) / 2)
        lower_mid = int(len(lst) / 2) - 1
        return mean([lst_sorted[lower_mid], lst_sorted[upper_mid]])

odd_list = [13, 18, 13, 14, 13, 16, 14, 21, 13]
even_list = [15, 14, 10, 8, 12, 8, 16, 13]

# print(sorted(odd_list))
# print(median(odd_list))
# print()
# print(sorted(even_list))
# print(median(even_list))




house_prices = [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]

# print(sorted(house_prices))
# print(f'Mean: {round(mean(house_prices))}')
# print(f'Median: {round(median(house_prices))}')

def mode(lst):
    modal_val = lst[0]

    for item in lst[1:]:
        if lst.count(item) >= lst.count(modal_val):
            modal_val = item
    
    return modal_val

mode_lst = ['swimming', 'juggling', 'skydiving', 'baseball', 'fencing', 'fencing', 'skydiving', 'juggling', 'skydiving', 'baseball', 'fencing', 'fencing', 'skydiving', 'juggling', 'juggling', 'zebra watching', 'skydiving', 'fencing', 'zebra watching','zebra watching','zebra watching','zebra watching']

# print(mode(mode_lst))
# print(max(mode_lst))



# print(set(mode_lst))
# print(max(set(mode_lst), key=mode_lst.count))



from random import choice

sample_range = list(range(0, 99+1))

samples = []

for _ in range(5):
    samples.append(choice(sample_range))

# print(f'Mu: {mean(sample_range)}')
# print(f'xbar:{mean(samples)}')


def five_number_summary(lst):
    return min(lst), median(sorted(lst)[0:int(len(lst)/2)]), median(lst), median(sorted(lst)[int(len(lst)/2)+(len(lst) % 2):]), max(lst)


even_test_dat = list(range(0, 99+1))
odd_test_dat = list(range(0, 100+1))

# print(five_number_summary(even_test_dat))
# print(five_number_summary(odd_test_dat))



a = [15,2,9,5,6,7,27,12,18,19,1]
b = [6,1,4,51,7,16,10,14,46,22,24,56,48,54]


def output_breakout(lst):
    print(sorted(lst))
    print(five_number_summary(lst))
    print(mean(lst))
    print(median(lst))
    print()

# output_breakout(a)
# output_breakout(b)



def iqr(lst):
    _, q1, _, q3, _ = five_number_summary(lst)
    return q3 - q1

a = list(range(0, 50+1, 5)) 
b = list(range(0, 100+1, 5))

print(a)
print(median(a))
print(iqr(a))
print
print(b)
print(median(b))
print(iqr(b))


