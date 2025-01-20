def solve_puzzle(pairs):
    from collections import defaultdict
    
    graph = defaultdict(list)
    in_degree = {}
    out_degree = {}
    
    for a, b in pairs:
        graph[a].append(b)
        out_degree[a] = out_degree.get(a, 0) + 1
        in_degree[b] = in_degree.get(b, 0) + 1
    
    start_nodes = [node for node in graph if out_degree[node] - in_degree.get(node, 0) == 1]
    end_nodes = [node for node in graph if in_degree.get(node, 0) - out_degree[node] == 1]
    
    if not (len(start_nodes) <= 1 and len(end_nodes) <= 1):
        return "IMPOSSIBLE"
    
    start_node = start_nodes[0] if start_nodes else next(iter(graph))
    
    path = []
    stack = [start_node]
    
    while stack:
        node = stack[-1]
        if not graph[node]:
            path.append(node)
            stack.pop()
        else:
            next_node = graph[node].pop()
            stack.append(next_node)
    
    if len(path) != len(pairs):
        return "IMPOSSIBLE"
    
    for i in range(len(path) - 1):
        if path[i] == pairs[i][0]:
            continue
        else:
            for j in range(len(path) - 1):
                if path[i] == pairs[j][1]:
                    pairs[i], pairs[j] = pairs[j], pairs[i]
                    break
    
    result = ""
    for node in path:
        result += node
    
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    case_number = 0
    while data:
        k = int(data[0])
        pairs = []
        for i in range(1, k + 1):
            a, b = data[i].split()
            pairs.append((a, b))
        case_number += 1
        result = solve_puzzle(pairs)
        print(f"Case {case_number}: {result}")
        data = data[k + 1:]

if __name__ == "__main__":
    main()