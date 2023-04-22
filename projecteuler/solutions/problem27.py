# https://projecteuler.net/problem=27
# Find the product of the coefficients, a and b, for the quadratic
# expression that produces the maximum number of primes for consecutive 
# values of n, starting with n = 0
# (|a| < 1000, |b| <= 1000)

from functools import cache
#from collections import Counter

@cache
def isprime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for j in range(2, n):
        if j**2 > n:
            return True
        if n % j == 0:
            return False
    return False
        
def max_num_primes():
    lim = 1000
    a_best, b_best, numprimes_best = -lim, -(lim+1), 0
    for a in range(-(lim-1), lim):
        for b in range(-lim, lim+1):
            n = 0
            while True:
                number = (n**2) + (a*n) + b
                if not isprime(number):
                    if n > numprimes_best:
                        a_best, b_best, numprimes_best = a, b, n
                    break
                n += 1
    return a_best*b_best

if __name__ == '__main__':
    print(max_num_primes())