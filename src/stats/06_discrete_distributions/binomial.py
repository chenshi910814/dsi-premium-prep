
binary = [0, 1]
four_bit_binary = []

for bit1 in binary:
    for bit2 in binary:
        for bit3 in binary:
            for bit4 in binary:
                four_bit_binary.append([bit1, bit2, bit3, bit4])

# for bin_ in four_bit_binary:
#     print(bin_)

def dec_to_bin(dec, n_bits=8):
    bit_list = []
    x = dec

    for _ in range(n_bits):
        bit = x % 2
        bit_list.append(bit)
        x //= 2

    return bit_list[::-1]

# print(dec_to_bin(43, n_bits=8))


def get_binary(n_bits=8):
    bins_d = dict()

    for dec in range(2**n_bits):
        bins_d[dec] = dec_to_bin(dec, n_bits)
        # print(f'{dec}: {bins_d[dec]}')
    return bins_d

# for dec, bin_ in get_binary(n_bits=8).items():
#     print(f'{dec}: {bin_}')



