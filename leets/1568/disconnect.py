# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/description/


def minDays(grid):
    m, n = len(grid), len(grid[0])
    visited = [[False] * n for _ in range(m)]
    islands = 0

    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or grid[i][j] == 0:
            return
        visited[i][j] = True
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                islands += 1

    if islands == 1:
        return 0
    elif islands == 0:
        return -1  # grid is already disconnected (all water)
    else:
        return islands - 1


# def minDays(grid):
#     """
#     :type grid: List[List[int]]
#     :rtype: int
#     """
#     m = len(grid)
#     n = len(grid[0])

#     grid = Grid(grid)
#     if len(grid.islands) > 1:
#         return 0
#     days = grid.disconnect()
#     return days


# class GridBox:
#     def __init__(self, i, j, value, island = None):
#         self.row = i
#         self.col = j
#         self.value = value
#         self.set_island(island)

#     def disconnect(self):
#         self.value = 0
#         self.island.remove(self)

#     def set_island(self, island):
#         self.island = island
#         if self.island is not None:
#             self.island.add(self)


# class Island:
#     def __init__(self, grid):
#         self.gridBoxes = []
#         self.grid = grid

#     def add(self, gridBox):
#         self.gridBoxes.append(gridBox)

#     def remove(self, gridBox):
#         self.gridBoxes.remove(gridBox)

#     def disconnect(self):
#         if len(self.gridBoxes) == 1:
#             self.gridBoxes[0].disconnect()
#         else:
#             self.gridBoxes[1].disconnect()

#     def evaluate(self):
#         islands = []

#         for i, box in enumerate(self.gridBoxes):
#             disconnectedTop = True
#             disconnectedLeft = True

#             if box.row > 0 and self.grid[box.row-1][box.col].value == 1:
#                 disconnectedTop = False

#             if box.col > 0 and self.grid[box.row][box.col-1].value == 1:
#                 disconnectedLeft = False
            
#             if disconnectedTop and disconnectedLeft and i != 0:
#                 island = Island(self.grid)
#                 island.add(box)

#                 islands.append(island)
#             elif box.island not in islands:
#                 islands.append(box.island)

#         return islands
                       

# class Grid:
#     def __init__(self, grid):
#         self.gridBoxes = []
#         self.islands = []
#         self.init(grid)


#     def init(self, grid):
#         m = len(grid)
#         n = len(grid[0])

#         for i, row in enumerate(grid):
#             rowBoxes = []
#             self.gridBoxes.append(rowBoxes)

#             for j, item in enumerate(row):
#                 currentGrid = grid[i][j]

#                 if currentGrid == 1:
#                     if i > 0 and grid[i-1][j] == 1:
#                         gridBox = GridBox(i, j, currentGrid, self.gridBoxes[i-1][j].island)
#                     elif j > 0 and grid[i][j-1] == 1:
#                         gridBox = GridBox(i, j, currentGrid, self.gridBoxes[i][j-1].island)
#                     else:
#                         gridBox = GridBox(i, j, currentGrid, Island(self.gridBoxes))
#                         self.islands.append(gridBox.island)
#                 else:
#                     gridBox = GridBox(i, j, currentGrid)
                
#                 rowBoxes.append(gridBox)

#     def disconnect(self):
#         days = 0

#         if len(self.islands) > 1:
#             return days
#         else:
#             islands = self.islands
#             while len(islands) == 1:
#                 islands[0].disconnect()
#                 days += 1
#                 islands = islands[0].evaluate()

#         return days



grid = [
    [1,1,0,1,1],
    [1,1,1,1,1],
    [1,1,0,1,1],
    [1,1,0,1,1]
]


minDays(grid)
