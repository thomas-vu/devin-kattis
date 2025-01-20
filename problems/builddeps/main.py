from collections import defaultdict, deque
import sys

def read_input():
    n = int(sys.stdin.readline().strip())
    rules = defaultdict(list)
    for _ in range(n):
        line = sys.stdin.readline().strip()
        parts = line.split(':')
        file = parts[0].strip()
        dependencies = parts[1].split() if len(parts) > 1 else []
        rules[file] = dependencies
    changed_file = sys.stdin.readline().strip()
    return rules, changed_file

def topo_sort(rules, start):
    visited = set()
    stack = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            stack.append(node)
            for dep in rules[node]:
                if dep not in visited:
                    queue.append(dep)
    return stack

def main():
    rules, changed_file = read_input()
    order = topo_sort(rules, changed_file)
    print('\n'.join(order))

if __name__ == "__main__":
    main()