from projecteuler.solutions import problem7

def test_nth_prime():
    n = 10001
    assert problem7.nth_prime(n) == 104743
    