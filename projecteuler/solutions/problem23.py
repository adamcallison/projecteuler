# https://projecteuler.net/problem=23
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from projecteuler.solutions import util

def sum_of_all_non_two_abaundant_sums():
    MAX = 28_123
    abundant = []
    for j in range(1, MAX+1):
        divisor_sum = sum(util.divisors(j))
        if divisor_sum > j:
            abundant.append(j)
    two_abundant_sums = set()
    for j in range(len(abundant)-1):
        for k in range(j, len(abundant)):
            if abundant[j] + abundant[k] > MAX:
                break
            two_abundant_sums.add(abundant[j] + abundant[k])
    res = sum(num for num in range(1, MAX+1) if not num in two_abundant_sums)
    return res 
    
if __name__ == '__main__':
    print(sum_of_all_non_two_abaundant_sums())


