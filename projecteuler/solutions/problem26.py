# https://projecteuler.net/problem=26
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def cycle_length(j):
    remainder = 1
    remainders = {remainder:0}
    while True:
        remainder = (10*remainder) % j
        if (remainder == 0) or (remainder in remainders):
            break
        remainders[remainder] = len(remainders)
    
    if remainder == 0:
        return 0
    return len(remainders) - remainders[remainder]

def longest_cycle_d_lt_n(n):
    maximum_cycle_length, max_j = 0, -1
    for j in range(2, n):
        cl = cycle_length(j)
        if cl > maximum_cycle_length:
            maximum_cycle_length = cl
            max_j = j
    return max_j

if __name__ == '__main__':
    n = 1000
    print(longest_cycle_d_lt_n(n))


