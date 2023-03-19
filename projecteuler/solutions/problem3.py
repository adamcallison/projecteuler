# https://projecteuler.net/problem=3
# What is the largest prime factor of the number 600851475143 ?

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

def largest_prime_factor_of(n):
    sqrtn = int(math.ceil(math.sqrt(n)))
    primes_upto_sqrtn = sieve_of_eratosthenes(sqrtn)
    decomp = prime_decomposition(n, primes_upto_sqrtn)
    return max(decomp.keys())

if __name__ == '__main__':
    #n = 600851475143
    n = 6
    print(largest_prime_factor_of(n))


