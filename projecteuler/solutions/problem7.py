# https://projecteuler.net/problem=7
# What is the 10 001st prime number?

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

def nth_prime(n):
    curr = n
    primes = []
    while len(primes) < n:
        primes = sieve_of_eratosthenes(curr)
        curr *= 2
    return primes[n-1]
    
if __name__ == '__main__':
    n = 10001
    print(nth_prime(n))


