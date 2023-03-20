# https://projecteuler.net/problem=9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

import math

def product_of_pythagorean_triplet_summing_to_1000():
    for a in range (1, 999):
        for b in range(a+1, 1000 - a):
            c = 1000 - (a + b)
            if (a**2) + (b**2) == (c**2): return a, b, c, a*b*c
    
if __name__ == '__main__':
    print(product_of_pythagorean_triplet_summing_to_1000())


