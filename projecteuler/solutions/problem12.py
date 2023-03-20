# https://projecteuler.net/problem=12
# What is the value of the first triangle number to have over five hundred divisors?

from projecteuler.solutions import util

def first_triangle_number_over_n_divisors(n):
    j, triangle_number = 1, 0
    while True:
        triangle_number += j
        decomp = util.prime_decomposition(triangle_number)
        num_of_prime_factors = sum(decomp.values())
        num_of_divisors = 1
        for num in decomp.values():
            num_of_divisors *= num + 1
        if num_of_divisors > n: break
        j += 1
    return triangle_number

if __name__ == '__main__':
    n = 500
    print(first_triangle_number_over_n_divisors(n))


