import sys
from collections import defaultdict, deque

def generate_random(r, a, b, c):
    return (r * a + b) % c

def bfs(start, graph):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node] - visited)
    return len(visited)

def main():
    while True:
        try:
            line = sys.stdin.readline().strip()
            if not line:
                break
            n, r, a, b, c = map(int, line.split())
            
            graph = defaultdict(set)
            for _ in range(n):
                x = generate_random(r, a, b, c) % n
                y = generate_random(r, a, b, c) % n
                while x == y:
                    x = generate_random(r, a, b, c) % n
                    y = generate_random(r, a, b, c) % n
                graph[x].add(y)
                graph[y].add(x)
            
            groups = []
            visited = set()
            for i in range(n):
                if i not in visited:
                    size = bfs(i, graph)
                    groups.append((size, i))
                    visited.update(graph[i])
            
            groups.sort(key=lambda x: (-x[0], str(x[1])))
            output = []
            for size, _ in groups:
                count = groups.count((size, -1))
                if count == 1:
                    output.append(str(size))
                else:
                    output.append(f"{size}x{count}")
            print(" ".join(output))
        except EOFError:
            break

if __name__ == "__main__":
    main()