from projecteuler.solutions import problem26

def test_longest_cycle_d_lt_n():
    n = 1000
    assert problem26.longest_cycle_d_lt_n(n) == 983