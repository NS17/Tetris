import os

def print_field(matrix, obj=None):
    if obj is None:
        obj = []
    for y,x in obj:
        prev = matrix[x][y]
        matrix[x][y] = 1

    os.system('cls')
    for row in matrix:
        s = ''
        for val in row:
            if val:
                s += '#'
            else:
                s += ' '
        print(s)

    for y,x in obj:
        matrix[x][y] = prev