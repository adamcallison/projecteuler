from projecteuler.solutions import problem25

def test_first_fibonacci_n_digits():
    n = 1000
    assert problem25.first_fibonacci_n_digits(n) == 4782