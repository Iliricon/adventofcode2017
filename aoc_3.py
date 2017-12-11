import numpy as np
import math

def print_grid(grid):
    for line in grid:
        print(line)

def grid_surrounding(grid, y, x):
    _value = 0
    _value += grid[y-1][x-1]
    _value += grid[y-1][x]
    _value += grid[y-1][x+1]
    _value += grid[y][x-1]
    _value += grid[y][x]
    _value += grid[y][x+1]
    _value += grid[y+1][x-1]
    _value += grid[y+1][x]
    _value += grid[y+1][x+1]
    return _value

n = 23 

grid = [[0 for i in range(n)] for i in range(n)]

x = int(n/2)
y = int((n-1)/2)

value = 1
grid[x][y] = value

print_grid(grid)

y = y+1


try:
    while value <= 277678:
        print(str(x) + "|" + str(y))
        value = grid_surrounding(grid, x, y)
        grid[x][y] = value
        if (grid[x][y-1] != 0 and grid[x-1][y] != 0):
            y += 1
        elif (grid[x][y-1] != 0) and (grid[x-1][y] == 0):
            x -= 1
        elif (grid[x+1][y] != 0):
            y -= 1
        elif (grid[x][y+1] != 0):
            x += 1
        else:
            y += 1
        
except IndexError:
    print("DONE")

with open("thegrid.txt", "w") as g:
    for item in grid:
        g.write("%s\n" % item)

print_grid(grid)
print(value)

