""" un/comment to de/activate ################

# evaluation/execution
# types
# abstractions
    # classe
    # functions
    # variables

# control flow
    # if elif else
# iteration
    # loops


# simple class
class stats_tools:
    def factorial(n):
        prod = 1
        for i in range(2, n+1):
            prod *= i

        return prod

    def permutations(n, r):
        return int( stats_tools.factorial(n) / stats_tools.factorial(n - r) )

    def combinations(n, r):
        return int( stats_tools.factorial(n) /
        ( stats_tools.factorial(n - r) *
          stats_tools.factorial(r) ) )


# len(lst)
# lst.count(el)
# lst.append(el)
# stats_tools.factorial()

# OOP(ish) class
class Binomial:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.expected_value = n * p
        self.variance = n * p * (1 - p)
        self.stdv = self.variance**(1/2)


    def __repr__(self):
        return f"where n={self.n} and p={self.p} variance={self.variance}"


    def pmf(self, k):
        n, p = self.n, self.p
        return stats_tools.combinations(n, k) * (p**k) * ((1 - p)**(n - k))


    def cdf(self, k):
        n, p = self.n, self.p
        acc = 0
        for i in range(k):
            acc += self.pmf(i)

        return acc


# flip a coin 10 times
some_n = 10
some_p = 0.5
ten_flips = Binomial(some_n, some_p)

# print( ten_flips ) # <day_11_lib.Binomial object at 0x7fb32272efd0>
# print( ten_flips.n )
# print( ten_flips.p )
# print( ten_flips.expected_value )
# print( ten_flips.variance )
# print( ten_flips.stdv )

some_k = 8
print( ten_flips.cdf(some_k) )
# print( ten_flips.pmf_dict[some_k] )


########################################## """
