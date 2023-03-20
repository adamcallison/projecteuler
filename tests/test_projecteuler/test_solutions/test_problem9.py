from projecteuler.solutions import problem9

def test_product_of_pythagorean_triplet_summing_to_1000():
    assert problem9.product_of_pythagorean_triplet_summing_to_1000() == (200, 375, 425, 200*375*425)
    