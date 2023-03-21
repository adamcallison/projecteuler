from projecteuler.solutions import problem15

def test_num_routes():
    width, height = 20, 20
    assert problem15.num_routes(width, height) == 137_846_528_820
    