# https://projecteuler.net/problem=5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math

def sieve_of_eratosthenes(n):
    remaining = set(range(2, n+1))
    p = 2
    while p**2 <= n:
        for j in range(p**2, n+1, p):
            try:
                remaining.remove(j)
            except KeyError:
                pass
        for j in range(p+1, n+1):
            if j in remaining:
                p = j
                break
    result = list(remaining)
    result.sort()
    return result

def prime_decomposition(n, primes_upto_sqrtn):
    decomp = {}
    left = n
    for p in primes_upto_sqrtn:
        if p > math.sqrt(left): break
        count = 0
        while left % p == 0:
            left //= p
            count += 1
        if count > 0: decomp[p] = count
    if left > 1:
        decomp[left] = 1
    return decomp

def smallest_evenly_divisible_up_to(n):
    primes = sieve_of_eratosthenes(n)
    prime_factors = {}
    for j in range(2, n+1):
        decomp = prime_decomposition(j, primes)
        print(j, decomp)
        for p, count in decomp.items():
            prime_factors[p] = max(prime_factors.get(p, 0), count)
    result = 1
    for p, count in prime_factors.items():
        result *= p**count
    return result

if __name__ == '__main__':
    n = 20
    print(smallest_evenly_divisible_up_to(n))


