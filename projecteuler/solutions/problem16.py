# https://projecteuler.net/problem=16
# What is the sum of the digits of the number 2**1000?

def sum_digits_of_power_of_two(power):
    prod_register = [2]
    carry = 0
    for j in range(1, power):
        k = 0
        while (k < len(prod_register)) or carry:
            if k == len(prod_register): prod_register.append(0)
            digit = (prod_register[k]*2) + carry
            carry, digit = digit // 10, digit % 10
            prod_register[k] = digit
            k += 1
    return sum(prod_register)
            
if __name__ == '__main__':
    power = 1000
    print(sum_digits_of_power_of_two(power))


