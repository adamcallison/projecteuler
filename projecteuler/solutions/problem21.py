# https://projecteuler.net/problem=21
# Evaluate the sum of all the amicable numbers under 10000.

from projecteuler.solutions import util

def sum_amicable_under(n):
    res = 0
    divisor_sums = {}
    for a in range(1, n):
        if not a in divisor_sums:
            divisors = util.divisors(a)
            divisor_sum = sum(divisors)
            divisor_sums[a] = divisor_sum
        else:
            divisor_sum = divisor_sums[a]
        b = divisor_sum
        if b <= a:
            continue
        if not b in divisor_sums:
            divisors = util.divisors(b)
            divisor_sum = sum(divisors)
            divisor_sums[b] = divisor_sum
        else:
            divisor_sum = divisor_sums[b]

        if a == divisor_sum:
            res += a
            if b < n:
                res += b
    return res

if __name__ == '__main__':
    n = 10_000
    print(sum_amicable_under(n))


