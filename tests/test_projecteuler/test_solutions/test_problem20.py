from projecteuler.solutions import problem20

def test_sum_digits_factorial():
    n = 100
    assert problem20.sum_digits_factorial(n) == 648
    