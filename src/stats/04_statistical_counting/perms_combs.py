
def factorial(n):
    prod = 1
    for num in range(2, n+1):
        prod *= num
    return prod

# print(factorial(5))


# print(factorial(10))

# print(1 / factorial(10))


def permutations(n, k):
    return int(factorial(n) / factorial(n-k))




print(permutations(600, 110))