from projecteuler.solutions import problem12

def test_first_triangle_number_over_n_divisors():
    n = 500
    assert problem12.first_triangle_number_over_n_divisors(n) == 76_576_500
    