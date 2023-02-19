
"""
prompt: https://leetcode.com/problems/number-of-islands/

example cases:
    example 1:
        Input: grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
        ]
        Output: 1

    example 2:
        Input: grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        Output: 3
"""

from collections import deque

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited = [[False for entry in row] for row in grid]
        
        # traverse and mark nodes as visited
        def traverse(row, col):
            visitNext = deque()
            for neighbor in getNeighbors(row, col):
                visitNext.append(neighbor)
            while visitNext:
                current = visitNext.popleft()
                for neighbor in getNeighbors(current[0], current[1]):
                    if not visited[current[0]][current[1]]: visitNext.append(neighbor)
                visited[current[0]][current[1]] = True
            return None

        # get valid neighbors for this matrix format
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

        islandCount = 0

        # main loop over all nodes
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j]:
                    if grid[i][j] == "0":
                        visited[i][j] = True
                    else:
                        traverse(i, j)
                        islandCount += 1
        return islandCount
    
