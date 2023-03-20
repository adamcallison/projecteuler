# This file contains tools that are used for more than one problem

class PrimeNumberGenerator:
    def __init__(self, max_increment=None):
        self.__primes__ = [2, 3, 5, 7]
        self.__calculated__ = 7
        self.__max_increment__ = max_increment
        
    def __call__(self, n):
        if n < 1: raise ValueError("n must be 1 or greater")
        while n > len(self.__primes__):
            self.__calculate__()
        return self.__primes__[n-1]
        
    def __calculate__(self):
        if self.__max_increment__ is None:
            calculate_up_to = self.__calculated__*2
        else:
            calculate_up_to = min(self.__calculated__*2, self.__calculated__ + self.__max_increment__)
        start = (self.__calculated__+ 1) if (self.__calculated__ % 2 == 0) else (self.__calculated__+ 2)
        integers = set(range(start, calculate_up_to + 1, 2))
        for p in self.__primes__[1:]:
            if p**2 > calculate_up_to:
                break
            coeff = (start) // p
            curr = (coeff*p) if (coeff*p % 2 == 1) else ((coeff*p) + p)
            curr = max(curr, p**2)
            while curr <= calculate_up_to:
                try: integers.remove(curr)
                except KeyError: pass
                curr += 2*p
        new_primes = list(integers)
        new_primes.sort()
        self.__primes__.extend(new_primes)
        self.__calculated__ = calculate_up_to
        return 
_prime_number_generator = PrimeNumberGenerator(max_increment=10000000)
def prime_number(n):
    if n < 1: raise ValueError("n must be 1 or greater")
    return _prime_number_generator(n)

def prime_decomposition(n):
    decomp = {}
    left = n
    j, p = 1, prime_number(1)
    while p**2 <= left:
        count = 0
        while left % p == 0:
            left //= p
            count += 1
        if count > 0: decomp[p] = count
        j += 1
        p = prime_number(j)
    if left > 1: decomp[left] = 1
    return decomp