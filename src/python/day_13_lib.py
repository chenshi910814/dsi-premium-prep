# """un/comment to de/activate ###########################

# types
    # int, float
    # bool
    # None
    # str
    # tuple

    # list
    # dict
    # set

# abstractions
    # variables
    # functions
    # classes
        # attributes
            # stateful
                # properties
            # logical
                # methods

# control flow
# iteration

#######################################################"""
# """un/comment to de/activate ###########################

# classes
# OOP

# extra time
# try / except / raise


#######################################################"""
"""un/comment to de/activate ###########################

# simple class
class stats_tools:
    def factorial(n):
        prod = 1
        for i in range(2, n+1):
            prod *= i

        return prod


    def combinations(n, r):
        return stats_tools.factorial(n) / ( stats_tools.factorial(n - r) * stats_tools.factorial(r) )


# binomial
class Binomial:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.expected_value = n * p
        self.variance = n * p * (1 - p)
        self.stdv = self.variance**(1/2)
        self.pmf_dict = {}


    def pmf(self, k):
        n = self.n
        p = self.p
        return stats_tools.combinations(n, k) * (p**k) * ((1 - p)**(n - k))


    def calculate_pmf_dict():
        for i in range(self.n+1):
            self.pmf_dict[i] = self.pmf(i)


    def cdf(self, k):
        acc = 0
        for i in range(k+1):
            acc += self.pmf(i)

        return acc


##########################################################

some_n = 10
some_p = 0.5
ten_flips = Binomial(some_n, some_p) # class initialization
print( ten_flips.expected_value )
print( ten_flips.variance )
print( ten_flips.stdv )

print( ten_flips.pmf(4) )
print( ten_flips.cdf(4) )
# TypeError: pmf() takes 1 positional argument but 2 were given
# print( ten_flips ) # <day_13_lib.Binomial object at 0x7ff892ff0dc0>


def binomial_pmf(n, k, p):
    return stats_tools.combinations(n, k) * (p**k) * ((1 - p)**(n - k))

print( binomial_pmf(10, 4, 0.5) )


binomial_pmf_d = {}
def pmf_dict(n, k, p):
    for i in range(n+1):
        binomial_pmf_d[i] = binomial_pmf(i)


#######################################################"""
# """un/comment to de/activate ###########################


def adderator(a, b):
    if list in (type(a), type(b)):
        raise "can't add with a list"

    return a + b


print( adderator("hello", " world") )
print( adderator(10, 7) )
print( adderator(10, [7]) )
# print( adderator(10, "hello") ) # "10 hello"




#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
# """un/comment to de/activate ###########################



#######################################################"""
