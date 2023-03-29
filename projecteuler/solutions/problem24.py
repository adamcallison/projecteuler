# https://projecteuler.net/problem=24
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

from projecteuler.solutions import util

def _nth_lexicographic_permutation(n, symbols):
    if n == 1:
        return symbols
    m = len(symbols)
    mm1factorial = util.factorial(m-1)
    first_symbol_idx = (n-1) // mm1factorial
    first_symbol = symbols[first_symbol_idx]
    remaining_symbols = [
        symbol for j, symbol in enumerate(symbols) if not j == first_symbol_idx
        ]
    remaining_solved = _nth_lexicographic_permutation(
        n-(first_symbol_idx*mm1factorial), 
        remaining_symbols
        )
    return [first_symbol] + remaining_solved

def nth_lexicographic_permutation(n, symbols):
    return ''.join(_nth_lexicographic_permutation(n, list(symbols)))
    
if __name__ == '__main__':
    n, symbols = 1_000_000, '0123456789'
    print(nth_lexicographic_permutation(n, symbols))


