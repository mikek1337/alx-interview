#!/usr/bin/python3
""" N queens problem """
import sys


def printSolution(board):
    """ Print the solution """
    queens = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                queens.append([i, j])
    print(queens)


def isSafe(board, row, col):
    """ Check if a queen can be placed on board[row][col] """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solveNQUtil(board, col):
    """ Solve N Queen problem """
    if col == len(board):
        printSolution(board)
        return True
    res = False
    for i in range(len(board)):
        if isSafe(board, i, col):
            board[i][col] = 1
            res = solveNQUtil(board, col + 1) or res
            board[i][col] = 0
    return res


def solveNQ(n):
    """ Solve N Queen problem """
    if n < 4:
        print("N must be at least 4")
        return False
    board = [[0 for i in range(n)] for j in range(n)]
    solveNQUtil(board, 0)


if __name__ == "__main__":
    solveNQ(int(sys.argv[1]))
