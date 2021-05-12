from random import choice

def get_bit():
    return choice([0,1])

def get_binary():
    bit_list = []

    for _ in range(16):
        bit_list.append(get_bit())

    return bit_list

print(get_binary())