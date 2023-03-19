# https://projecteuler.net/problem=2
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def sum_of_even_fibonacci_below(n):
    result, f1, f2 = 0, 1, 2
    while f2 <= n:
        if f2 % 2 == 0: result += f2
        f1, f2 = f2, f1+f2
    return result

if __name__ == '__main__':
    n = 4000000
    print(sum_of_even_fibonacci_below(n))


