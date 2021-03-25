from random import choice


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



def binomial_distr(n_trials=8):
    binomial_dict = dict()

    bin_dict = get_binary(n_bits=n_trials)

    for _, bin_list in bin_dict.items():
        sum_bits = sum(bin_list)
        if sum_bits not in binomial_dict:
            binomial_dict[sum_bits] = 0
        binomial_dict[sum_bits] += 1

    return binomial_dict

d = binomial_distr(n_trials=12)

# for k, cnt in d.items():
#     print(f'{k}: {cnt}')

'''
What is the probability of 5 heads in 12 coin flips of a fair coin?
n = 12
p = 0.5
'''
# print(d[5] / sum(d.values()))

# for k, cnt in d.items():
#     print(f'{k}: {round(cnt / sum(d.values()), 5)}')


# n = 12
# k = 9
# p = 0.5

# # print(d[9] / sum(d.values()))

# accum = 0.0
# for k in range(0, 4+1):
#     accum += d[k] / sum(d.values())
# print(accum)



def get_bit():
    return choice([0,1])

def generate_n_bits(n=8):
    return [get_bit() for _ in range(n)]
    
    # lst = []
    # for _ in range(n):
    #     lst.append(get_bit())
    # return lst

# print(generate_n_bits(n=8))


def binary_sampling_dict(num_bits=8, num_samples=1000):
    d = dict()

    for _ in range(num_samples):
        binary = generate_n_bits(num_bits)
        num_successes = sum(binary)

        if num_successes not in d:
            d[num_successes] = 1
        else:
            d[num_successes] += 1
        
    return d

d = binary_sampling_dict(num_bits=8, num_samples=1000000)

for k, cnt in sorted(d.items()):
    print(f'{k}: {cnt}')