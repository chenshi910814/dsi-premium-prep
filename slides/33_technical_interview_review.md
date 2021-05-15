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
