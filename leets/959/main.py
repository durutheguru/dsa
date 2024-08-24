from union_find import *


def countRegionsBySlashes(grid):
    n = len(grid)
    uf = UnionFind(4 * n * n)

    for i in range(n):
        for j in range(n):
            root = 4 * (i * n + j)  # Calculate the starting index for the current cell
            val = grid[i][j]
            
            # Connect internal triangles based on the character
            if val == '/':
                uf.union(root, root + 3)  # Top to left
                uf.union(root + 1, root + 2)  # Right to bottom
            elif val == '\\':
                uf.union(root, root + 1)  # Top to right
                uf.union(root + 2, root + 3)  # Bottom to left
            else:  # ' '
                uf.union(root, root + 1)  # Connect all parts together
                uf.union(root + 1, root + 2)
                uf.union(root + 2, root + 3)
            
            # Connect to the right cell's left triangle
            if j + 1 < n:
                uf.union(root + 1, 4 * (i * n + j + 1) + 3)
            # Connect to the bottom cell's top triangle
            if i + 1 < n:
                uf.union(root + 2, 4 * ((i + 1) * n + j))
        
    return uf.get_count()

grid=[['/','\\'],['\\','/']]
print("Grid regions: ", countRegionsBySlashes(grid))
