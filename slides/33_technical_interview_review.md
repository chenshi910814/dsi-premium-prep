# TI Skills/Outline
* The Interview
* Expected Skills


<br><br><br><br><br><br><br>

----------------------------------------------------
# The Interview
* At this time, the timed portion of the interview is 45 minutes 
* Write Python functions that explore statistical or probability concepts

<br><br><br><br><br><br><br>

----------------------------------------------------
# textbook problems re: Discrete Distrs and Probability
* Recognize and solve problems related to:
    * Binomial
    * Poisson
    * Geometric
    * Uniform
    * Bayes Theorem


<br><br><br><br><br><br><br>

----------------------------------------------------
# Understanding Sampling Approaches
* Understanding counting or binary through the lens of independent trials
    * binary ex: [0,1,1,0,1] <- each "coin flip or bit is independent of the other, if each bit is randomly generated"
    * trinary ex: [0, 1, 1, 2, 0]


<br><br><br><br><br><br><br>

----------------------------------------------------
# Coding mathematical formulations
* We will provide you any functions you'll need to code.
  
  
<br><br><br><br><br><br><br>

----------------------------------------------------
# Analysis through Dictionaries
* Pack values into dictionaries
    * Check membership vs not checking membership
* Transform Dictionary values
* General analytic approach
    * Create generative process
    * Load results into a dict
    * Interpret/Transform


<br><br><br><br><br><br><br>

----------------------------------------------------
# Interpret Results
* May involve recognizing a pattern
* Might involve introduction to a new statistical concept and interpreting results through that concept.



<br><br><br><br><br><br><br>

----------------------------------------------------
# Practice
* let's review functions and particular problems



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)
*  Code the `mean()` function
* BONUS: Include a `trim` parameter that removes the greatest and least `n` values

* Test with this data:

```python
a = [1, 5, 7, 10, 15, 23, 35, 67, 220, 2000]
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def mean(lst, trim_by=0):
    lst_ = lst.copy()

    if trim_by > 0:
        
        lst_ = sorted(lst_)[trim_by:-trim_by]

    return sum(lst_) / len(lst_)
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (6 minutes)
* Code the `median()` function. Make sure to account for even and odd length lists.


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION

```python
def median(lst):
    lst_sorted = sorted(lst)

    # if odd
    if len(lst) % 2 == 1:
        mid = int(len(lst) / 2)
        return lst_sorted[mid]
    else:
        upper_mid_idx = int(len(lst)/2)
        return mean([lst_sorted[upper_mid_idx-1], lst_sorted[upper_mid_idx]])
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)
Code the `variance()` function. Make sure to include a parameter that determines whether the data is a sample or population, and apply Bessel's correction accordingly


* **Population Variance**:

$$
\sigma^2 = \frac{1}{n} \sum_{i=1}^{n} (x_i - \mu)^2
$$

* **Sample Variance**:

$$
s^2 = \frac{1}{n-1} \sum_{i=1}^{n} (x_i - \overline x)^2
$$

* Recall:
    * $\mu$ : population mean
    * $\overline x$ : sample mean


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (4 minutes)

```python
def variance(lst, sample=True):
    mean_ = mean(lst)

    total = 0

    for item in lst:
        total += (item - mean_)**2

    if sample:
        return total / (len(lst) - 1)
    else:
        return total / len(lst)
```


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (2 minutes)
Code the `stdev()` function. Make sure to include a parameter that determines whether the data is a sample or population, and apply Bessel's correction accordingly

* **Population Standard Deviation**:

$$
\sigma = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (x_i - \mu)^2}
$$

* **Sample Standard Deviation**:

$$
s = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \overline x)^2}
$$

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT SOLUTION
Code the `stdev()` function. Make sure to include a parameter that determines whether the data is a sample or population, and apply Bessel's correction accordingly

```python
def stdev(lst, sample=True):
    return variance(lst, sample)**(1/2)
```



<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes) code `factorial()`


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT Solution

```python
def factorial(num):
    prod = 1
    for n in range(2, num+1):
        prod *= n
    return prod
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)
Code the `permutations(n,k)` function

$nPk = \frac{n!}{(n-k)!}$


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT Solution
Code the `permutations(n,k)` function

```python
def permutations(n, k):
    return int(factorial(n) / factorial(n-k))
```

Slightly more optimized:

```python
def permutations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return perm
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)
Write a permutations story problem


<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)
Code the `combinations Function`

$$
nCk = \frac{n!}{((n-k)! k!)}
$$

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT Solution
Code the `combinations Function`

$$
nCk = \frac{n!}{((n-k)! k!)}
$$

```python
def combinations(n, k):
    return int(factorial(n) / (factorial(n-k) * factorial(k)))

# Slightly more optimal:
def combinations(n, k):
    perm = 1
    for i in range(n, n-k, -1):
        perm *= i
    return int(perm / factorial(k))
```

<br><br><br><br><br><br><br><br><br>

---------------------------------------------------------------
# BREAKOUT (3 minutes)
Write a combinations story problem


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (4 minutes)
Code the `bernoulli()` function. It should take one argument, `p_success`.

You will want to use `from random import random`. The `random()` function will return a uniformly distributed random float between 0 and 1.


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (4 minutes)
Code the `bernoulli()` function. It should take one argument, `p_success`.

```python
def bernoulli(p_success=0.5):
    draw = random() # gets a val betw 0 and 1

    if draw < p_success:
        return True
    else:
        return False
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (4 minutes)
Code the `get_list_of_bits()` function. It should take one argument, `n_bits`, and it should return a list containing random 1s and 0s.


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT SOLUTION

```python
from random import choice

def get_bit():
    return choice([0,1])

def generate_n_bits(n=8):
    return [get_bit() for _ in range(n)]
    # lst = []
    # for _ in range(n):
    #     lst.append(get_bit())
    # return lst
```

<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (4 minutes)
#### Write a function called binary_sampling_dict that has two params
* `num_bits=8`
* `num_samples=1000`

return a `dict` where the keys represent the number of successes,
and the values associated with those keys represent the count
of that number of successes occurring.

```python
{
    0: 35,
    1: 63,
    ...
    num_bits: count of num_bits successes
}

# 00101101 : 4 successes
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution
#### Write a function called binary_sampling_dict that has two params
* `num_bits=8`
* `num_samples=1000`

```python
def binary_sampling_dict(num_bits=8, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_bits(num_bits)
        observed_k = sum(binary)

        if observed_k not in d:
            d[observed_k] = 0
        d[observed_k] += 1

    return d
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (3 minutes)
### Code the Binomial PMF (`binomial_pmf(n,p,k)`)
* 3 parameters
$n$ = number of bernoulli trials
$p$ = probability of success on any given bernoulli trial
$k$ = specific number of successes for which to find the probability

$$
P(X=k) = {n \choose k} p^k(1-p)^{n-k}
$$


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution
### Code the Binomial Distribution 

```python
def binomial_pmf(n, k, p=0.5):
    return combinations(n, k) * (p**k) * (1-p)**(n-k)
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (4 minutes) 
### Code the Binomial CDF (`binomial_cdf(n, k_high, p=0.5)`)

$$
P(X \le k) = \sum_{i=0}^k {n \choose i}p^i(1-p)^{n-i}
$$


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution
### Code the Binomial CDF (`binomial_pmf(n, k_high, p=0.5)`)

```python
def binomial_cdf(n, k_high, p=0.5):
    cumulative = 0.0

    for k in range(0, k_high+1):
        cumulative += binomial_pmf(n, k, p)

    return cumulative
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (5 minutes)
#### Code the `binomial_pmf_dict()` function.
This should take 4 parameters:
* `n`: the number of trials
* `k_low`: the low value of $k$ in the dictionary
* `k_high`: the high value of $k$ in the dictionary
* `p=0.5`: the probability of success of a given bernoulli trial


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution

```python
def binomial_pmf_dict(n, k_low, k_high, p=0.5):
    d = dict()

    for k in range(k_low, k_high+1):
        d[k] = binomial_pmf(n, k, p)

    return d

d = binomial_pmf_dict(8, 0, 8, p=0.25)

for k, v in d.items():
    print(f'{k}: {v}')
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (4 minutes)
Code the `poisson_pmf()` function.
* $e = 2.71828$
* Note, both the constant `e` and the `factorial()` function are available from the `math` module.


$$
P(\lambda, k \text{ events}) = \frac{e^{-\lambda}\lambda^k}{k!}
$$


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution
Code the `poisson_pmf()` function.
Note, both the constant `e` and the `factorial()` function are available from the `math` module.

$$
P(\lambda, k \text{ events}) = \frac{e^{-\lambda}\lambda^k}{k!}
$$


```python
from math import e, factorial

# print(e) # 2.718281828459045

def poisson_pmf(lmbda, k):
    return lmbda**k * e**(-lmbda) / factorial(k)
```


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (5 minutes)
#### Code the `poisson_cdf` function


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution
#### Code the `poisson_cdf` function

```python
def poisson_cdf(lmbda, k_high):
    cdf = 0.0

    for k in range(k_high+1):
        cdf += poisson_pmf(lmbda, k)

    return cdf
```

<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT (6 minutes)
#### Code the `poisson_pmf_dict()`
* your parameters will be 
    * `lmbda`
    * `low_k`
    * `high_k`

Holding `lmbda` constant, write a function that returns a dictionary showing the probs for number of events from `low_k` to `high_k` (inclusive)


<br><br><br><br><br><br><br><br><br><br>
---------------------------------------
# BREAKOUT Solution

```python
def poisson_pmf_dict(lmbda, low_k, high_k):
    d = dict()

    for k in range(low_k, high_k+1):
        d[k] = poisson_pmf(lmbda, k)

    return d

d = poisson_pmf_dict(10, 0, 30)

for k, v in d.items():
    print(f'{k}: {round(v, 6)}')
```



<br><br><br><br><br><br><br><br>

--------------------------------
# BREAKOUT (4 minutes)
Code the `geometric_pmf()` function
* `p` : probability
* `k` : number of failures (inclusive or exclusive of the 1st success)
* `inclusive=True` : whether or not to use inclusive or exclusive pmf

PMF calculating the number of trials up to **and including** the first success

$$
P(X=k) = p (1-p)^{k-1}
$$

PMF calculating the number of trials **before** the first success

$$
P(X=k) = p (1-p)^{k}
$$

<br><br><br><br><br><br><br><br>

--------------------------------
# BREAKOUT Solution
Code the `geometric_pmf()` function
* `p` : probability
* `k` : number of failures (inclusive or exclusive of the 1st success)
* `inclusive=True` : whether or not to use inclusive or exclusive pmf

```python
def geometric_pmf(p, k, inclusive=True):
    return p * (1-p)**(k-inclusive)
    # if inclusive:
    #     return p * (1-p)**(k-1)
    # else:
    #     return p * (1-p)**k
```


<br><br><br><br><br><br><br><br>

--------------------------------
# BREAKOUT (5 minutes)
Code 2 Functions

`geom_cdf_accum(p, k, inclusive=True)`
This function should use the PMF functions in an accumulator pattern


`geom_cdf_closed(p, k, inclusive=True)`
This function should use the CDF formulas: 
* up to **and including** the first success
    * $P(X \le k) = 1 - (1-p)^{k}$
* **before** the first success
    * $P(X \lt k) = 1 - (1-p)^{k+1}$


<br><br><br><br><br><br><br><br>

--------------------------------
# BREAKOUT Solution

```python
def geom_cdf_accum(p, k, inclusive=True):
    proba = 0.0

    if inclusive:
        starting_at = 1
    else:
        starting_at = 0

    for r in range(starting_at, k+1):
        proba += geometric_pmf(p, r, inclusive)

    return proba


def geom_cdf_closed(p, k, inclusive=True):
    if inclusive:
        return 1 - (1-p)**k
    else:
        return 1 - (1-p)**(k+1)
```



<br><br><br><br><br><br><br><br>

--------------------------------
# BREAKOUT (4 minutes)
##### Code the `geometric_pmf_dict(p, k_high, inclusive=True)` function


<br><br><br><br><br><br><br><br>

--------------------------------
# BREAKOUT Solution
##### Code the `geometric_pmf_dict(p, k_high, inclusive=True)` function

```python
def geometric_pmf_dict(p, k_high, inclusive=True):
    d = dict()

    for k in range(inclusive, k_high+1):
        d[k] = geometric_pmf(p, k, inclusive)

    return d

d_incl = geometric_pmf_dict(p=0.5, k_high=10, inclusive=True)
d_excl = geometric_pmf_dict(p=0.5, k_high=10, inclusive=False)

for k, v in d_excl.items():
    print(f'{k}: {v}')
```

<br><br><br><br><br><br><br><br>

--------------------------------
# BREAKOUT (4 minutes)
##### Code the `geometric_cdf_dict(p, k_high, inclusive=True)` function


<br><br><br><br><br><br><br><br>

--------------------------------
# BREAKOUT Solution
##### Code the `geometric_cdf_dict(p, k_high, inclusive=True)` function

```python
def geometric_cdf_dict(p, k_high, inclusive=True):
    d = dict()

    for k in range(inclusive, k_high+1):
        d[k] = geom_cdf_closed(p, k, inclusive)

    return d

d_incl = geometric_cdf_dict(p=0.5, k_high=100, inclusive=True)
d_excl = geometric_cdf_dict(p=0.5, k_high=10, inclusive=False)

for k, v in d_incl.items():
    print(f'{k}: {v}')
```







