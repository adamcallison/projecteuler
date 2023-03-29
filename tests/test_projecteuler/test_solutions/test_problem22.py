from projecteuler.solutions import problem22

import os

def test_total_name_score():
    with open(f"{os.path.dirname(__file__)}/../../../data/p022_names.txt", 'r') as f:
        names = f.read().replace('"','').strip().split(',')
    assert problem22.total_name_score(names) == 871_198_282
    