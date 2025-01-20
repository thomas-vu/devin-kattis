def count_hamiltonian_cycles(n, k, forbidden_edges):
    # This is a placeholder function to simulate the problem's requirements.
    # In this simplified version, we will generate all possible cycles and count those that don't include forbidden edges.
    # Since the problem is simplified, we can use a brute-force approach for n up to 10.
    
    def generate_cycles(graph, visited, start):
        count = 0
        for neighbor in graph[start]:
            if (start, neighbor) not in forbidden_edges and (neighbor, start) not in forbidden_edges:
                if len(visited) == n - 1:
                    count += 1
                else:
                    visited.add(neighbor)
                    count += generate_cycles(graph, visited, neighbor)
                    visited.remove(neighbor)
        return count
    
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in forbidden_edges:
        graph[u].append(v)
        graph[v].append(u)
    
    total_cycles = 0
    for i in range(1, n + 1):
        visited = set([i])
        total_cycles += generate_cycles(graph, visited, i)
    
    return total_cycles % 9901

def main():
    T = int(input())
    for case_num in range(1, T + 1):
        n, k = map(int, input().split())
        forbidden_edges = [tuple(map(int, input().split())) for _ in range(k)]
        result = count_hamiltonian_cycles(n, k, forbidden_edges)
        print("Case #{}: {}".format(case_num, result))

if __name__ == "__main__":
    main()