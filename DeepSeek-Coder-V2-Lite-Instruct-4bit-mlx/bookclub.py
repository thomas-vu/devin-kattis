# This problem can be solved using a graph-based approach where each member is a node and the likes are edges.
# We need to check if there's an Eulerian cycle in the graph, which would mean that we can find a cycle where everyone trades books.
# We'll use Depth-First Search (DFS) to check for cycles and determine if the graph is Eulerian.

from collections import defaultdict

def dfs(node, visited, graph):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)

def can_everyone_trade(N, likes):
    graph = defaultdict(list)
    for a, b in likes:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * N
    dfs(0, visited, graph)  # Start DFS from any node (here we choose node 0)
    
    for i in range(N):
        if not visited[i]:  # If any node is not visited, the graph is not connected
            return "NO"
    
    # Check if every node has the same number of edges (since each edge represents a like)
    for i in range(N):
        if len(graph[i]) % 2 != 0:  # If the degree of any node is odd, it's not possible to form a cycle
            return "NO"
    
    return "YES"

# Read input
N, M = map(int, input().split())
likes = [list(map(int, input().split())) for _ in range(M)]

# Output the result
print(can_everyone_trade(N, likes))