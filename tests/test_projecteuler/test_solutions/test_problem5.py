from projecteuler.solutions import problem5

def test_smallest_evenly_divisible_up_to():
    n = 20
    assert problem5.smallest_evenly_divisible_up_to(n) == 232792560
    