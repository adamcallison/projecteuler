# https://projecteuler.net/problem=20
# Find the sum of the digits in the number 100!

def sum_digits_factorial(n):
    product = [1]
    carry = 0
    for j in range(2, n+1):
        k = 0
        while (k < len(product)) or carry:
            if k == len(product): product.append(0)
            digit = (product[k]*j) + carry
            digit, carry = digit % 10, digit // 10
            product[k] = digit
            k += 1
    return sum(product)

if __name__ == '__main__':
    n = 100
    print(sum_digits_factorial(n))


