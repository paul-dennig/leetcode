import copy
from collections import deque

def updateMatrix(mat):
    dist_mat = deepcopy(mat)

    for i in len(mat):
        for j in len(mat[i]):
            if not mat[i][j] == 0:
                dist_mat[i][j] = dist(mat, i, j)

    return dist_mat

def dist(mat, row, col):
    num_rows = len(mat)
    num_cols = len(mat[row])
    visited = set([row, col])
    next_up = deque([[row, col]])

    while next_up:
        current = next_up.popleft()
        visited.add(current)
        neighbors = current.getNeighbors(current[0], current[1], num_rows, num_cols)

        print("hi")

    return mat

def getNeighbors(row, col, num_rows, num_cols):
    neighbors = []
    if isValid(row-1, col, x_size, y_size): neighbors.append([row-1, col])
    if isValid(row+1, col, x_size, y_size): neighbors.append([row+1, col])
    if isValid(row, col-1, x_size, y_size): neighbors.append([row, col-1])
    if isValid(row, col+1, x_size, y_size): neighbors.append([row, col+1])
    return neighbors

def isValid(row, col, num_rows, num_cols):
    return (0 <= row < y_size) and (0 <= col < x_size)

def test():


test()
