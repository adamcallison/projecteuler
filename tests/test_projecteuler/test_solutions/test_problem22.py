from projecteuler.solutions import problem22

from urllib.request import urlopen

def test_total_name_score():
    fileurl = 'https://projecteuler.net/project/resources/p022_names.txt'
    names = str(urlopen(fileurl).read()).replace('"','').replace("'",'').replace("b", '').strip().split(',')
    assert problem22.total_name_score(names) == 871_198_282
    