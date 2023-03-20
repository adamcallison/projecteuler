# https://projecteuler.net/problem=10
# Find the sum of all the primes below two million.

try:
    from . import util
except ImportError:
    import util

def sum_of_primes_below(n):
    j, tot = 1, 0
    while True:
        p = util.prime_number(j)
        if p >= n: break
        tot += p
        j += 1
    return tot
    
if __name__ == '__main__':
    n = 2_000_000
    print(sum_of_primes_below(n))


