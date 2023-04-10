# https://projecteuler.net/problem=25
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def first_fibonacci_n_digits(n):
    fpre, f, idx = 1, 1, 2
    while len(str(f)) < n:
        fpre, f = f, fpre + f
        idx += 1
    return idx

if __name__ == '__main__':
    n = 1000
    print(first_fibonacci_n_digits(n))


