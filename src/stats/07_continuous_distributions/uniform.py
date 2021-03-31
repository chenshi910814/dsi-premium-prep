from random import choice

def get_bit():
    return choice([0,1])

def get_binary(n=8):
    return [get_bit() for _ in range(n)]

print(get_binary(4))