from collections import deque

def numIslands(grid):
    """Counts the number of islands in a grid."""
    m, n = len(grid), len(grid[0])
    visited = set()
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or (i, j) in visited:
            return
        visited.add((i, j))
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and (i, j) not in visited:
                count += 1
                dfs(i, j)
    return count

def is_critical_point(grid, i, j):
    """Checks if a land cell is a critical point."""
    m, n = len(grid), len(grid[0])
    grid[i][j] = 0
    count = numIslands(grid)
    grid[i][j] = 1
    return count > 1

def minDays(grid):
    """Returns the minimum number of days to disconnect the grid."""
    if numIslands(grid) == 1:
        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and is_critical_point(grid, i, j):
                    count += 1
        return count
    return 0



grid = [
    [1,1,0,1,1],
    [1,1,1,1,1],
    [1,1,0,1,1],
    [1,1,0,1,1]
]

print("Min Days: ", minDays(grid))

