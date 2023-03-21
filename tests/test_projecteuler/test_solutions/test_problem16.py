from projecteuler.solutions import problem16

def test_sum_digits_of_power_of_two():
    power = 1000
    assert problem16.sum_digits_of_power_of_two(power) == 1366
    