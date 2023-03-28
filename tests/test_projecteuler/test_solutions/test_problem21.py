from projecteuler.solutions import problem21

def test_sum_amicable_under():
    n = 10_000
    assert problem21.sum_amicable_under(n) == 31_626
    