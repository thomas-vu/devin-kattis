def clean_feathers(ponds, channels, queries):
    from collections import defaultdict
    import sys
    input = sys.stdin.readline
    
    # Build the graph
    graph = defaultdict(list)
    for a, b, f in channels:
        graph[a].append((b, f))
        graph[b].append((a, f))
    
    # Function to perform DFS and clean feathers
    def dfs(start, end):
        visited = set()
        stack = [(start, 0)]  # (current_pond, cleaned_feathers)
        while stack:
            pond, feathers = stack.pop()
            if pond == end:
                return bin(feathers).count('1')
            if pond not in visited:
                visited.add(pond)
                for neighbor, filter_value in graph[pond]:
                    stack.append((neighbor, feathers | filter_value))
        return -1
    
    # Process queries
    answers = []
    for start, end in queries:
        answer = dfs(start, end)
        answers.append(answer)
    
    return answers

# Read input
N, M, Q = map(int, input().split())
channels = [tuple(map(int, input().split())) for _ in range(M)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# Get the answers and print them
answers = clean_feathers(N, channels, queries)
for answer in answers:
    print(answer)