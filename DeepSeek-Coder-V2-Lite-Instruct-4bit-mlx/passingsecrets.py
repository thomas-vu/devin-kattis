from collections import defaultdict, deque

def parse_input():
    groups = defaultdict(set)
    while True:
        try:
            line = input().split()
            if len(line) < 2: continue
            a, b = line[0], line[1]
            n = int(input())
            for _ in range(n):
                members = input().split()
                for member in members:
                    groups[member].update(members)
        except EOFError:
            break
    return groups

def bfs(groups, start, end):
    queue = deque([(start, [])])
    visited = set()
    while queue:
        node, path = queue.popleft()
        if node == end:
            return len(path), path + [end]
        if node not in visited:
            visited.add(node)
            for neighbor in groups[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [node]))
    return "impossible", []

def main():
    groups = parse_input()
    while True:
        try:
            a, b = input().split()
            risk, path = bfs(groups, a, b)
            if risk == "impossible":
                print("impossible")
            else:
                print(risk)
                print(' '.join(path))
        except EOFError:
            break

if __name__ == "__main__":
    main()