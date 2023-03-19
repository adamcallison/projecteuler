from projecteuler.solutions import problem3

def test_largest_prime_factor_of():
    n = 600851475143
    assert problem3.largest_prime_factor_of(n) == 6857
    