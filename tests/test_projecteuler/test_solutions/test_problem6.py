from projecteuler.solutions import problem6

def test_diff_sumsquares_squaresum_upto():
    n = 100
    assert problem6.diff_sumsquares_squaresum_upto(n) == 25164150
    