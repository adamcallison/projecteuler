# https://projecteuler.net/problem=5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

from projecteuler.solutions import util

def smallest_evenly_divisible_up_to(n):
    prime_factors = {}
    for j in range(2, n+1):
        decomp = util.prime_decomposition(j)
        for p, count in decomp.items():
            prime_factors[p] = max(prime_factors.get(p, 0), count)
    result = 1
    for p, count in prime_factors.items():
        result *= p**count
    return result

if __name__ == '__main__':
    n = 20
    print(smallest_evenly_divisible_up_to(n))


