from math import sqrt

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

    mid = int(len(lst) / 2)
    # odd
    if len(lst) % 2:
        return lst_sorted[mid]
    else:
        return mean([lst_sorted[mid-1], lst_sorted[mid]])


# print(sorted(odd_list))
# print(median(odd_list))

# print()

# print(sorted(even_list))
# print(median(even_list))


'''
An issue of a recent magazine reported the following home sale amounts for a sample of homes in Alameda, CA, all of which were sold in the previous month (1000s of $):

{ 590, 615, 575, 608, 350, 1285, 408, 540, 555, 679 }
'''

house_prices = [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]

# print(sorted(house_prices))
'''
a. Find the mean value of the homes sold in April
'''
# print(f'house price mean: {round(mean(house_prices))}')

'''
b. Find the median value of the homes sold in April
'''
# print(f'house price mean: {round(median(house_prices))}')
'''

c. Do you think mean or median is a “better” measure of center for this data? why?
'''


animals = ['frog', 'cat', 'dog', 'beaver', 'cat', 'cat', 'beaver', 'beaver', 'lizard', 'lizard']


def mode(lst):
    most_occurring = lst[0]
    for item in lst[1:]:
        if lst.count(item) > lst.count(most_occurring):
            most_occurring = item
    return most_occurring

# print(mode(animals))


from random import choice

sample_range = list(range(0, 99+1))
n_samps = 15
samples = []

for _ in range(n_samps):
    samples.append(choice(sample_range))

# print(f'pop mean: {mean(sample_range)}')
# print(f'sample mean: {mean(samples)}')
# print(f'sample med: {median(samples)}')





def five_number_summary(lst):
    min_ = min(lst)
    max_ = max(lst)
    med = median(lst)

    sorted_lst = sorted(lst)

    odd = len(lst) % 2
    
    lower_half = sorted_lst[0: int(len(lst) / 2)]
    upper_half = sorted_lst[int(len(lst) / 2) + odd: ]

    q1 = median(lower_half)
    q3 = median(upper_half)

    return min_, q1, med, q3, max_


# samp_data = list(range(1,101))

# print(five_number_summary(samp_data))



def iqr(lst):
    _, q1, _, q3, _ = five_number_summary(lst)
    return q3 - q1

a = list(range(0, 50+1, 5)) 
b = list(range(0, 100+1, 5))

# print(median(a))
# print(iqr(a))
# print(iqr(b))


def detect_outliers(lst, outlier_coef=1.5):
    _, q1, _, q3, _ = five_number_summary(lst)
    iqr_ = iqr(lst)    

    outliers = []

    for num in lst:
        if num < q1 - outlier_coef*iqr_:
            outliers.append(num)
        if num > q3 + outlier_coef*iqr_:
            outliers.append(num)
    
    return outliers
        
test_outliers = list(range(0,100))
test_outliers.append(10_000)

# print(detect_outliers(test_outliers, outlier_coef=1.5))


def remove_outliers(lst, outlier_coef=1.5):
    output = lst.copy()
    outliers = detect_outliers(lst, outlier_coef=1.5)


    for num in outliers:
        if num in output:
            output.remove(num)

    return output

house_prices =  [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]

# print(remove_outliers(house_prices))



def variance(lst, sample=True):
    mean_ = mean(lst)
    total = 0.0

    for item in lst:
        total += (item - mean_)**2

    return total / (len(lst) - sample)

b = list(range(0, 100+1, 5))

# print(b)
# print(variance(b, sample=True))
# print(variance(b, sample=False))


def stdev(lst, sample=True):
    return sqrt(variance(lst, sample))



house_prices = [590, 615, 575, 608, 350, 1285, 408, 540, 555, 679]

# Find variance
print(f'Mean: {mean(house_prices)}')

print(f'Samp Var: {round(variance(house_prices))}')

# Find Stdev
print(f'Samp StDev: {round(stdev(house_prices))}')