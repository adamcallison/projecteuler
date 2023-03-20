# https://projecteuler.net/problem=3
# What is the largest prime factor of the number 600851475143 ?

from . import util

def largest_prime_factor_of(n):
    decomp = util.prime_decomposition(n)
    return max(decomp.keys())

if __name__ == '__main__':
    n = 600851475143
    print(largest_prime_factor_of(n))


