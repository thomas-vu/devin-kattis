# Solution in Python 3
class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
        self.transpose_adj = [[] for _ in range(V)]
        self.complement_adj = [set() for _ in range(V)]
    
    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.transpose_adj[v].append(u)
        if u != v:
            self.complement_adj[u].add(v)
            self.complement_adj[v].add(u)
    
    def remove_edge(self, u, v):
        self.adj[u].remove(v)
        self.transpose_adj[v].remove(u)
        self.complement_adj[u].discard(v)
        self.complement_adj[v].discard(u)
    
    def get_outdegree(self, u):
        return len(self.adj[u])
    
    def get_hash(self, u):
        neighbors = self.adj[u] if len(self.adj[u]) > 0 else [0]
        hash_value = sum(7**i * n for i, n in enumerate(neighbors)) % (10**9 + 7)
        return hash_value
    
    def get_complement(self):
        new_graph = Graph(self.V)
        for u in range(self.V):
            for v in range(u + 1, self.V):
                if v not in self.complement_adj[u] and u not in self.complement_adj[v]:
                    new_graph.add_edge(u, v)
        return new_graph
    
    def get_transpose(self):
        new_graph = Graph(self.V)
        for u in range(self.V):
            for v in self.transpose_adj[u]:
                new_graph.add_edge(v, u)
        return new_graph
    
    def __str__(self):
        result = ""
        for u in range(self.V):
            outdegree = self.get_outdegree(u)
            neighbors_hash = self.get_hash(u)
            result += f"{outdegree} {neighbors_hash}\n"
        return result.strip()

def main():
    V, E, Q = map(int, input().split())
    graph = Graph(V)
    
    for _ in range(E):
        u, v = map(int, input().split())
        graph.add_edge(u, v)
    
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            graph.adj.append([])
            graph.transpose_adj.append([])
            graph.complement_adj.append(set())
            V += 1
        elif query[0] == 2:
            graph.add_edge(query[1], query[2])
        elif query[0] == 3:
            graph.adj[query[1]] = []
            graph.transpose_adj[query[1]] = []
            graph.complement_adj[query[1]] = set()
        elif query[0] == 4:
            graph.remove_edge(query[1], query[2])
        elif query[0] == 5:
            graph = graph.get_transpose()
        elif query[0] == 6:
            graph = graph.get_complement()
    
    print(V)
    for u in range(V):
        outdegree = graph.get_outdegree(u)
        neighbors_hash = graph.get_hash(u)
        print(f"{outdegree} {neighbors_hash}")

if __name__ == "__main__":
    main()