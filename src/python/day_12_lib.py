"""un/comment to de/activate ###########################

'''
Suppose you have a fair coin and you flip it 10 times, what is the probability that there will be 6 or more heads as a result of these 10 flips?

We want to represent the below equation in python, where n is the number of trials, k is the number of successes and p is the probability of a success.
'''
def factorial(n):
    prod = 1
    for i in range(1, n+1):
        prod *= i
    return prod

def combinations(n, r):
    return int( factorial(n) / (factorial(n - r) * factorial(r)) )

def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * ((1 - p)**(n - k))

def binomial_cdf(n, k, p=0.5):
    acc = 0
    for i in range(k+1):
        acc += binomial_pmf(n, i, p)

    return acc

n = 10
k = 5
# print( 1 - binomial_cdf(n, k) )


# What is the probability that exactly 4 of the 15 randomly selected accidents involve only one vehicle?
print( binomial_pmf(15, 4, 0.7) ) # 0.0005805753776550008

# What is the probability that fewer than 4 of the 15 randomly selected accidents only involve one vehicle
print( binomial_cdf(15, 3, 0.7) ) # 9.165869215200015e-05

# What is the probability that 10 or more randomly selected accidents only involved one vehicle?
print( binomial_cdf(15, 9, 0.7) ) # 0.27837855979563614

# What is the probability that more than 5 and less than 8 of the 15 randomly selected accident involved only one vehicle?
print( binomial_pmf(15, 6, 0.7) + binomial_pmf(15, 7, 0.7) ) # 0.04636001904534003




#######################################################"""
"""un/comment to de/activate ###########################

def anagrams(arr):
    lst = []
    for word1 in arr:
        for word2 in arr:
            if word1 != word2\
            and sorted(word1) == sorted(word2)\
            and word1 not in lst:
                lst.append(word1)
    return lst


inp_lst = ['dog', 'god', 'cat', 'act', 'dog', 'tack', 'tack', 'star', 'rat', 'rats']
print( anagrams(inp_lst) )
# ['dog', 'god', 'cat', 'act', 'star', 'rats']

#######################################################"""
# """un/comment to de/activate ###########################
'''
Let’s create a function that sorts a given string,
where each word in the string will contain a single number.
This number is the position the word should have in the result. Numbers can be from 1 to 9, so the first word will have a 1 not a 0 in it.

If the string is empty, return an empty string, and the words in the input string will only contain valid consecutive numbers
'''

def order( txt ):
    tup_lst = []
    for word in txt.split():
        digits = ""
        for ch in word:
            if ch.isdigit():
                digits += ch
        tup_lst.append( (int(digits), word) )

    # return tup_lst

    return " ".join([ word for num, word in sorted(tup_lst) ] )


print( order("is2 Thi1s T4est 3a") ) # "Thi1s is2 3a T4est"
print( order("4of Fo1r pe6ople g3ood th5e the2") ) # "Fo1r the2 g3ood 4of th5e pe6ople"
print( order("4of Fo1r pe60ople g347ood th5e the2") ) # "Fo1r the2 4of th5e pe60ople g347ood"
print( order("") ) # ""


#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
