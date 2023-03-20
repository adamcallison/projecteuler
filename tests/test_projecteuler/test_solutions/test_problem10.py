from projecteuler.solutions import problem10

def test_sum_of_primes_below():
    n = 2_000_000
    assert problem10.sum_of_primes_below(n) == 142_913_828_922
    