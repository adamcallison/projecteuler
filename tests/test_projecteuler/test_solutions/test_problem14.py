from projecteuler.solutions import problem14

def test_longest_collatz_sequence_starting_below():
    n = 1_000_000
    assert problem14.longest_collatz_sequence_starting_below(n) == 837799
    