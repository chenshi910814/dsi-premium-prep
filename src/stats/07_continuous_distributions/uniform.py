from random import choice

def get_bit():
    return choice([0,1])

def get_binary(n=8):
    return [get_bit() for _ in range(n)]

binary = [1,1,1,1,1,1,1,1]#get_binary(n=8)

accum = 0.0

print(binary[0] * 0.5**1 + binary[1] * 0.5**2 + binary[2] * 0.5**3 + binary[3] * 0.5**4 + binary[4] * 0.5**5 + binary[5] * 0.5**6 + binary[6] * 0.5**7 + binary[7] * 0.5**8)