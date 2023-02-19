
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]

visited = [[0 for entry in row] for row in grid]

def getNeighbors(row, col):
    neighborList = []
    if row > 0 and grid[row-1][col] == "1": 
        neighborList.append([row-1, col])
    if row < len(grid) - 1 and grid[row+1][col] == "1": 
        neighborList.append([row+1, col])
    if col > 0 and grid[row][col-1] == "1": 
        neighborList.append([row, col-1])
    if col < len(grid[row]) - 1 and grid[row][col+1] == "1": 
        neighborList.append([row, col+1])
    return neighborList

print(getNeighbors(3, 3))