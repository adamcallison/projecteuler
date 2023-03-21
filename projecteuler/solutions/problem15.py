# https://projecteuler.net/problem=15
# How many such routes (top left to bottom right, moving only down or right) are there through a 20×20 grid?

def num_routes(width, height):
    column = [1]*(height+1)
    for j in range(1, width+1):
        prev_column, column = column, ([1] + ([0]*(height)))
        for k in range(1, height+1):
            column[k] = prev_column[k] + column[k-1]
    return column[-1]

if __name__ == '__main__':
    width, height = 20, 20
    print(num_routes(width, height))


