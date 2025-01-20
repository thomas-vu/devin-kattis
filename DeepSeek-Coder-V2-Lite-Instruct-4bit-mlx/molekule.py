def main():
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    
    # Create adjacency list to represent the graph
    adj_list = [[] for _ in range(N + 1)]
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    # Initialize the result array with zeros
    result = [0] * (N - 1)
    
    # Function to perform DFS and determine the direction of bonds
    def dfs(node, parent):
        for child in adj_list[node]:
            if child != parent:
                # Direct the bond from node to child
                result[child - 2] = 1
                dfs(child, node)
    
    # Start DFS from any node (here we start from node 1)
    dfs(1, -1)
    
    # Output the result
    for r in result:
        print(r)

if __name__ == "__main__":
    main()