
class UnionFind:

    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [1] * size
        self.count = size

    def find(self, x):
        if (x != self.parent[x]):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if (rootX != rootY):
            if (self.rank[rootX] > self.rank[rootY]):
                self.parent[rootY] = rootX
            elif (self.rank[rootY] > self.rank[rootX]):
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1

    def get_count(self):
        return self.count
    

