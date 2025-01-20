MOD = 9901

def count_hamiltonian_cycles(n, k, forbidden_edges):
    # Create adjacency matrix for the graph
    adj_matrix = [[0] * n for _ in range(n)]
    for u, v in forbidden_edges:
        adj_matrix[u-1][v-1] = 1
        adj_matrix[v-1][u-1] = 1
    
    def is_valid(path):
        visited = [False] * n
        for node in path:
            if visited[node]:
                return False
            visited[node] = True
        return True
    
    def count_cycles(path):
        if len(path) == n:
            return 1 if is_valid(path) else 0
        
        count = 0
        last_node = path[-1]
        for next_node in range(n):
            if adj_matrix[last_node][next_node] == 0:
                continue
            if next_node not in path and (last_node, next_node) not in forbidden:
                count += count_cycles(path + [next_node])
        return count
    
    total_count = 0
    for start in range(n):
        forbidden = set()
        for u, v in forbidden_edges:
            if u == start or v == start:
                forbidden.add((min(u, v), max(u, v)))
        total_count += count_cycles([start])
    
    return total_count % MOD

def main():
    T = int(input())
    for case_num in range(1, T + 1):
        n, k = map(int, input().split())
        forbidden_edges = [tuple(map(int, input().split())) for _ in range(k)]
        result = count_hamiltonian_cycles(n, k, forbidden_edges)
        print(f"Case #{case_num}: {result}")

if __name__ == "__main__":
    main()