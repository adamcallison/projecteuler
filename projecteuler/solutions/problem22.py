# https://projecteuler.net/problem=22
# What is the total of all the name scores in the file?

import os

def total_name_score(names):
    names = sorted(names)
    total = 0
    for j, name in enumerate(names):
        total += (j+1)*sum(ord(c) - 64 for c in name)
    return total
    
if __name__ == '__main__':
    with open(f"{os.path.dirname(__file__)}/../../data/p022_names.txt", 'r') as f:
        names = f.read().replace('"','').strip().split(',')
    print(total_name_score(names))


