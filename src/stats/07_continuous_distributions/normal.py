from math import e, pi, sqrt

def normal_pdf(x=0, mu=0, sigma=1):
    return (1 / (sigma * sqrt(2 * pi))) * e**(-(1/2) * ((x - mu) / sigma)**2)


# print(normal_pdf(0.5, 0, 1)) # ~0.3521



def normal_cdf(x=0, mu=0, sigma=1):
    x_width = 0.001
    x_vals = [num*x_width for num in range(-1000, int(x*1000))]
    accum = 0.0

    for x in x_vals:
        accum += normal_pdf(x, mu, sigma) * x_width
        if x > x:
            break
    return accum

print(normal_cdf(x=300, mu=475, sigma=98)) #-> ~0.371 (compared to z-table score of ~0.367)

