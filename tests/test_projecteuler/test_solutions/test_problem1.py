from projecteuler.solutions import problem1

def test_sum_of_3_5_multiples_below():
    n = 1000
    assert problem1.sum_of_3_5_multiples_below(n) == 233168
    