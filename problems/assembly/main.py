def can_form_unbounded(molecules):
    # Helper function to check if two edges are compatible
    def is_compatible(a, b):
        return (a[0] == b[0] and a[1] != b[1]) or (a[2] == b[2] and a[3] != b[3])
    
    # Create a graph where each molecule is a node and edges are connections
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    in_degree = {i: 0 for i in range(len(molecules))}
    out_degree = {i: 0 for i in range(len(molecules))}
    
    # Build the graph
    for i in range(len(molecules)):
        for j in range(i + 1, len(molecules)):
            if is_compatible(molecules[i], molecules[j]):
                graph[i].append(j)
                in_degree[j] += 1
                out_degree[i] += 1
            if is_compatible(molecules[j], molecules[i]):
                graph[j].append(i)
                in_degree[i] += 1
                out_degree[j] += 1
    
    # Check for unbounded structure using in-degrees and out-degrees
    start_nodes = [i for i in range(len(molecules)) if out_degree[i] > 0]
    end_nodes = [i for i in range(len(molecules)) if in_degree[i] > 0]
    
    # If both start and end nodes are present, the structure is unbounded
    return "unbounded" if len(start_nodes) > 0 and len(end_nodes) > 0 else "bounded"

# Read input
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
molecules = data[1:]

# Output the result
print(can_form_unbounded(molecules))