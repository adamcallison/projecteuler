# https://projecteuler.net/problem=1
# Find the sum of all the multiples of 3 or 5 below 1000.


def sum_of_3_5_multiples_below(n):
    curr, curr_sum = 3, 0
    add_for_3, add_for_5 = 3, 2
    while curr < n:
        curr_sum += curr
        if add_for_3 == add_for_5:
            curr += add_for_3
            add_for_3, add_for_5 = 3, 5
        elif add_for_3 < add_for_5:
            curr += add_for_3
            add_for_3, add_for_5 = 3, add_for_5 - add_for_3
        else:
            curr += add_for_5
            add_for_3, add_for_5 = add_for_3 - add_for_5, 5
    return curr_sum

if __name__ == '__main__':
    n = 1000
    print(sum_of_3_5_multiples_below(n))


