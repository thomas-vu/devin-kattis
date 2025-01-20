def explore_subway(s1, s2):
    def dfs(node, visited, path):
        if node in visited:
            return False
        visited.add(node)
        for neighbor, edge in graph[node]:
            if (neighbor, -edge) not in visited:
                path.append(str(edge))
                if dfs(neighbor, visited, path):
                    return True
                path.pop()
        visited.remove(node)
        return False
    
    def is_same_tree(s1, s2):
        n = len(s1)
        if n != len(s2):
            return False
        graph = {}
        for i in range(n):
            if s1[i] == '0':
                if (i, -1) not in graph:
                    graph[(i, 1)] = []
                if (i, -1) not in graph:
                    graph[(i, -1)] = []
                graph[(i, 1)].append((i + 1, -1))
                graph[(i, -1)].append((i - 1, 1))
            else:
                if (i, -1) not in graph:
                    graph[(i, 1)] = []
                if (i, -1) not in graph:
                    graph[(i, -1)] = []
                graph[(i, 1)].append((i - 1, -1))
                graph[(i, -1)].append((i + 1, 1))
            
            if s2[i] == '0':
                if (i, -1) not in graph:
                    graph[(i, 1)] = []
                if (i, -1) not in graph:
                    graph[(i, -1)] = []
                graph[(i, 1)].append((i + 1, -1))
                graph[(i, -1)].append((i - 1, 1))
            else:
                if (i, -1) not in graph:
                    graph[(i, 1)] = []
                if (i, -1) not in graph:
                    graph[(i, -1)] = []
                graph[(i, 1)].append((i - 1, -1))
                graph[(i, -1)].append((i + 1, 1))
        
        for i in range(n):
            if (0, -1) not in graph or (0, 1) not in graph:
                return False
            if dfs(0, set(), []):
                continue
            else:
                return False
        return True
    
    n = len(s1)
    if is_same_tree(s1, s2):
        return "same"
    else:
        return "different"

# Read input
t = int(input())
for _ in range(t):
    s1 = input()
    s2 = input()
    result = explore_subway(s1, s2)
    print(result)