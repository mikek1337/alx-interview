#!/usr/bin/python3
"""island parameter"""


def island_perimeter(grid):
    parameter = 0
    for i in range(len(grid)):
        print(grid[i])
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                parameter += 1
                if (grid[i][j+1] == 1 and grid[i-1][j] == 1):
                    parameter += 1
    return 2*parameter
