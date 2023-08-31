#!/usr/bin/python3
"""grid parameter"""


def island_perimeter(grid):
    """calculate the parameter of grid"""
    M, N = len(grid), len(grid[0])
    count = 0
    for i in range(0, M):
        for j in range(0, N):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    count = count + 1
                if i == M - 1 or grid[i + 1][j] == 0:
                    count = count + 1
                if j == 0 or grid[i][j - 1] == 0:
                    count = count + 1
                if j == N - 1 or grid[i][j + 1] == 0:
                    count = count + 1
    return count
