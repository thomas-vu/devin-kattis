import sys
from itertools import combinations

def read_ints():
    return list(map(int, sys.stdin.readline().strip().split()))

def read_graph():
    n, e = read_ints()
    weights = read_ints()
    edges = [tuple(read_ints()) for _ in range(e)]
    return n, e, weights, edges

def solve_naive(n, e, weights, edges):
    used = [False] * n
    for u, v in edges:
        if weights[u] < weights[v]:
            used[u] = True
        elif weights[u] > weights[v]:
            used[v] = True
        else:
            used[u] = True
    vertex_cover = [i for i in range(n) if used[i]]
    return sum(weights[v] for v in vertex_cover), vertex_cover

def main():
    n, e, weights, edges = read_graph()
    Val, vertex_cover_naive = solve_naive(n, e, weights, edges)
    
    min_weight = float('inf')
    best_cover = []
    
    for r in range(1, n + 1):
        for cover in combinations(range(n), r):
            if all((u, v) not in edges for u, v in zip(cover, cover[1:])):
                current_weight = sum(weights[v] for v in cover)
                if current_weight < min_weight:
                    min_weight = current_weight
                    best_cover = list(cover)
    
    print(min_weight)
    print(*best_cover)

if __name__ == "__main__":
    main()