from sys import stdin, stdout

def read_ints():
    return list(map(int, input().split()))

while True:
    n, m = read_ints()
    if n == 0 and m == 0:
        break
    
    adj_list = [[] for _ in range(n)]
    for _ in range(m):
        u, v = read_ints()
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    def is_possible():
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                stack = [i]
                visited[i] = True
                parent = {i: -1}
                while stack:
                    node = stack.pop()
                    for neighbor in adj_list[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            parent[neighbor] = node
                            stack.append(neighbor)
                        elif neighbor != parent[node]:
                            return True  # Cycle detected
        return False
    
    def dfs(start, target):
        stack = [(start, [start])]
        while stack:
            node, path = stack.pop()
            if node == target:
                return path
            for neighbor in adj_list[node]:
                if neighbor not in path:
                    stack.append((neighbor, path + [neighbor]))
        return None
    
    if not is_possible():
        print("Impossible")
    else:
        min_sequence = None
        for start in range(n):
            sequence = dfs(start, -1)
            if sequence and (min_sequence is None or len(sequence) < len(min_sequence)):
                min_sequence = sequence
            elif sequence and len(sequence) == len(min_sequence):
                min_sequence = min(min_sequence, sequence, key=lambda x: tuple(x))
        
        if min_sequence:
            print(f"{len(min_sequence)}:{' ' + ' '.join(map(str, min_sequence))}")
        else:
            print("Impossible")