# https://projecteuler.net/problem=6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def diff_sumsquares_squaresum_upto(n):
    s, ssq = 0, 0
    for j in range(1, n+1):
        s += j
        ssq += (j**2)
    return (s**2) - ssq

if __name__ == '__main__':
    n = 100
    print(diff_sumsquares_squaresum_upto(n))


