# https://projecteuler.net/problem=4
# Find the largest palindrome made from the product of two 3-digit numbers

import math

def largest_palindrome_product_3digit():
    largest = -1
    for j in range(100, 999):
        for k in range(j+1, 1000):
            prod = j*k
            prodstr = str(prod)
            if prodstr == prodstr[::-1]: largest = max(largest, prod)
    return largest

if __name__ == '__main__':
    print(largest_palindrome_product_3digit())


