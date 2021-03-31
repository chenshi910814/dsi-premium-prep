from random import choice

def get_bit():
    return choice([0,1])

def get_binary(n=8):
    return [get_bit() for _ in range(n)]

for i in range(1, 10+1):
    print(0.5**i)
    

# print(get_binary())