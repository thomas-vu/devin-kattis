def is_valid_proposal(m, roads):
    graph = {i: [] for i in range(m)}
    reverse_graph = {i: [] for i in range(m)}
    
    for a, b in roads:
        graph[a].append(b)
        reverse_graph[b].append(a)
    
    def dfs(node, visited, graph):
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                stack.extend(graph[current])
    
    visited = set()
    for i in range(m):
        if i not in visited:
            dfs(i, visited, graph)
    
    if len(visited) == m:
        return True
    
    for a, b in roads:
        if b in graph[a] and a in reverse_graph[b]:
            new_graph = {i: graph[i][:] for i in range(m)}
            new_graph[a].remove(b)
            new_reverse_graph = {i: reverse_graph[i][:] for i in range(m)}
            new_reverse_graph[b].remove(a)
            
            visited = set()
            dfs(i, visited, new_graph)
            
            if len(visited) == m:
                print("Case {}: {} {}".format(case_number, a, b))
                return False
    
    print("Case {}: invalid".format(case_number))
    return False

def main():
    case_number = 0
    while True:
        try:
            m, n = map(int, input().split())
            roads = [tuple(map(int, input().split())) for _ in range(n)]
            case_number += 1
            
            if is_valid_proposal(m, roads):
                print("Case {}: valid".format(case_number))
            else:
                is_valid_proposal(m, roads)
        except EOFError:
            break

if __name__ == "__main__":
    main()