# https://projecteuler.net/problem=22
# What is the total of all the name scores in the file?

from urllib.request import urlopen

def total_name_score(names):
    names = sorted(names)
    total = 0
    for j, name in enumerate(names):
        total += (j+1)*sum(ord(c) - 64 for c in name)
    return total
    
if __name__ == '__main__':
    fileurl = 'https://projecteuler.net/project/resources/p022_names.txt'
    names = str(urlopen(fileurl).read()).replace('"','').replace("'",'').replace("b", '').strip().split(',')
    print(total_name_score(names))


