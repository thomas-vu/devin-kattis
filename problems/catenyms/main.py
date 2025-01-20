from collections import defaultdict, deque
import sys

def find_compound_catenym(words):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    for word in words:
        start, end = word[0], word[-1]
        graph[start].append(end)
        out_degree[start] += 1
        in_degree[end] += 1
    
    start_nodes = [node for node in graph if out_degree[node] > in_degree.get(node, 0)]
    end_nodes = [node for node in graph if in_degree[node] > out_degree.get(node, 0)]
    
    if len(start_nodes) != len(end_nodes):
        return "***"
    
    for node in graph:
        if out_degree[node] != in_degree.get(node, 0):
            return "***"
    
    start_node = min(start_nodes) if start_nodes else words[0][0]
    path = []
    stack = [start_node]
    
    while stack:
        node = stack[-1]
        if not graph[node]:
            path.append(stack.pop())
        else:
            stack.append(graph[node].pop())
    
    return '.'.join(reversed(path))

def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        words = [sys.stdin.readline().strip() for _ in range(n)]
        result = find_compound_catenym(words)
        print(result)

if __name__ == "__main__":
    main()