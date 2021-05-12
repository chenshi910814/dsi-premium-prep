from random import choice

def get_bit():
    return choice([0,1])

def get_binary():
    bit_list = []

    for _ in range(16):
        bit_list.append(get_bit())

    return bit_list

# print(get_binary())

def get_float():
    bin_list = get_binary()

    float_accum = 0.0

    for idx, bit in enumerate(bin_list, 1):
        float_accum += bit * 0.5**idx

    return float_accum, bin_list

# print(get_float())