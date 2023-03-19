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

def largest_prime_factor_of(n):
    sqrtn = int(math.ceil(math.sqrt(n)))
    primes = sieve_of_eratosthenes(sqrtn)
    for prime in primes[::-1]:
        if n % prime == 0: return prime

if __name__ == '__main__':
    n = 600851475143
    print(largest_prime_factor_of(n))


