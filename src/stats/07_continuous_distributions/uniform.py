from math import e, sqrt

from random import choice

def get_bit():
    return choice([0,1])

def get_binary(n=8):
    return [get_bit() for _ in range(n)]

def get_float(num_bits=8):
    bin_ = get_binary(num_bits)
    flt = 0.0
    for expon, bit in enumerate(bin_, 1):
        flt += 0.5**expon * bit
    return flt

# print(get_float(16))
    
# print(get_binary())

