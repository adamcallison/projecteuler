from projecteuler.solutions import problem2

def test_sum_even_fibonacci_below():
    n = 4000000
    assert problem2.sum_of_even_fibonacci_below(n) == 4613732
    