# This is the largest header

## This is a slightly smaller header

##### this is a small header
Here's some text

**Here's some bold text**

*one asterisk is italic*

_an underscore will italicize_


------------------------------

# Slide topic
* item 1
* item 2
* item 3
    * subitem 1
    * subitem 2


------------------------------

# Make a codecell
* using 3 tick marks `

```python
def factorial(n):
    prod = 1
    for num in range(1, n+1):
        prod *= num
    return prod
```

------------------------------

# Poisson PMF
* Given an average rate $\lambda$, find the probability of some number of events $k$
* PMF:

$$
P(\lambda, k) = \frac{e^{-\lambda} \cdot \lambda^k}{k!}
$$