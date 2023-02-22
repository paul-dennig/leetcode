
from collections import deque

class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for entry in row] for row in grid]
        maxArea = 0


        def traverse(row, col):
            #bfs
            #track area
            islandArea = 0
            nextVisit = deque()
            nextVisit.append([row, col])
            while nextVisit:
                nextUp = nextVisit.popleft()
                if not visited[nextUp[0]][nextUp[1]]:
                    # get neighbors
                    for neighbor in getNeighbors(nextUp[0], nextUp[1]):
                        if not visited[neighbor[0]][neighbor[1]]:
                            nextVisit.append(neighbor)
                    islandArea += 1
                    visited[nextUp[0]][nextUp[1]] = True
                #
            return islandArea

        def getNeighbors(row, col):
            neighborList = []

            #enforce that we are in bounds
            #and then add neighbor if it is also island
            
            #above
            if row > 0 and grid[row-1][col] == 1:
                neighborList.append([row-1, col])
            #below
            if row < len(grid) - 1 and grid[row+1][col] == 1:
                neighborList.append([row+1, col])
            #left
            if col > 0 and grid[row][col-1] == 1:
                neighborList.append([row, col-1])
            #right
            if col < len(grid[row]) - 1 and grid[row][col+1] == 1:
                neighborList.append([row, col+1])
            return neighborList

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if not visited[i][j]:
                    #move on if ocean, otherwise traverse island
                    if grid[i][j] == 1:
                        #update maxArea
                        maxArea = max(traverse(i, j), maxArea)
                    visited[i][j] = True
        return maxArea