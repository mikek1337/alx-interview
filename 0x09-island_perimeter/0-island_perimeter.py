#!/usr/bin/python3
"""island parameter"""


def island_perimeter(grid):
    """calculate the parameter of island"""
    parameter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                parameter += 1
                if (grid[i][j] != len(grid[i])):
                    if (grid[i][j+1] == 1 and grid[i-1][j] == 1):
                        parameter += 1
    if (len(grid) == 1):
        parameter = parameter*2
    return 2*parameter
