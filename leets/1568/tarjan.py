from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices            # Number of vertices
        self.graph = defaultdict(list) # Default dictionary to store graph
        self.time = 0                # Time variable used in DFS
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def find_articulation_points(self):
        disc = [-1] * self.V         # Store discovery times of visited vertices
        low = [-1] * self.V          # Store the earliest visited vertex reachable
        parent = [-1] * self.V       # Store parent vertices in DFS tree
        ap = [False] * self.V        # Boolean array to store articulation points
        
        for i in range(self.V):
            if disc[i] == -1:
                self.dfs(i, disc, low, parent, ap)
        
        # Articulation points are those vertices marked as True in ap[]
        for idx, is_ap in enumerate(ap):
            if is_ap:
                print(f"Articulation Point: {idx}")
    
    def dfs(self, u, disc, low, parent, ap):
        # Initialize discovery time and low value
        disc[u] = self.time
        low[u] = self.time
        self.time += 1
        children = 0  # Count of children in the DFS tree
        
        # Go through all vertices adjacent to u
        for v in self.graph[u]:
            # If v is not visited yet, make it a child of u in the DFS tree and recur for it
            if disc[v] == -1:
                parent[v] = u
                children += 1
                self.dfs(v, disc, low, parent, ap)
                
                # Check if the subtree rooted at v has a connection back to an ancestor of u
                low[u] = min(low[u], low[v])
                
                # u is an articulation point in the following cases:
                
                # (1) u is root of the DFS tree and has two or more children
                if parent[u] == -1 and children > 1:
                    ap[u] = True
                
                # (2) u is not root and low value of one of its children is more than discovery value of u
                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True
            
            # Update low[u] for back edge
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

# Example Usage
g = Graph(5)


g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(3, 5)
g.add_edge(4, 6)


#Fully Connected
# g.add_edge(0, 1)
# g.add_edge(0, 4)
# g.add_edge(1, 2)
# g.add_edge(1, 3)
# g.add_edge(1, 4)
# g.add_edge(3, 5)
# g.add_edge(3, 6)
# g.add_edge(4, 6)

# g.add_edge(2, 5)

g.find_articulation_points()

