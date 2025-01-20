def find_weak_vertices(graph):
    n = len(graph)
    weak_vertices = []
    
    for i in range(n):
        is_weak = True
        for j in range(n):
            if graph[i][j] == 1:
                for k in range(n):
                    if graph[j][k] == 1 and graph[i][k] == 1:
                        is_weak = False
                        break
                if not is_weak:
                    break
        if is_weak:
            weak_vertices.append(i)
    
    return weak_vertices

def main():
    while True:
        n = int(input())
        if n == -1:
            break
        
        graph = []
        for _ in range(n):
            row = list(map(int, input().split()))
            graph.append(row)
        
        weak_vertices = find_weak_vertices(graph)
        if weak_vertices:
            print(' '.join(map(str, sorted(weak_vertices))))

if __name__ == "__main__":
    main()