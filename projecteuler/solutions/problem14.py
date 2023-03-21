# https://projecteuler.net/problem=14
# Which starting number, under one million, produces the longest chain (Collatz sequence)?

def longest_collatz_sequence_starting_below(n):
    lengths = {1:1}
    stack = []
    max_length, max_start = 1, 1
    for j in range(2, n):
        curr = j
        while not curr in lengths:
            stack.append(curr)
            if curr % 2: curr = (3*curr)+1
            else: curr //= 2
        curr_length = lengths[curr]
        while stack:
            curr = stack.pop()
            curr_length += 1
            if curr_length > max_length:
                max_length = curr_length
                max_start = curr
            lengths[curr] = curr_length
    return max_start

if __name__ == '__main__':
    n = 1_000_000
    print(longest_collatz_sequence_starting_below(n))


