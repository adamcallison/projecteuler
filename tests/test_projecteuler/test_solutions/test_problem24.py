from projecteuler.solutions import problem24

def test_nth_lexicographic_permutation():
    n, symbols = 1_000_000, '0123456789'
    assert problem24.nth_lexicographic_permutation(n, symbols) == '2783915460'