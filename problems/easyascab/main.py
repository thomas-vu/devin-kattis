def find_alphabet_order(L, words):
    from collections import defaultdict
    
    # Create a graph to represent the order constraints
    graph = defaultdict(list)
    in_degree = {char: 0 for char in range(ord('a'), ord(L) + 1)}
    out_degree = {char: set() for char in range(ord('a'), ord(L) + 1)}
    
    # Compare each pair of words to find the order constraints
    for i in range(len(words) - 1):
        word1 = words[i]
        word2 = words[i + 1]
        min_len = min(len(word1), len(word2))
        
        for j in range(min_len):
            char1 = word1[j]
            char2 = word2[j]
            if char1 != char2:
                graph[char1].append(char2)
                in_degree[char2] += 1
                out_degree[char1].add(char2)
                break
        else:
            if len(word1) > len(word2):
                return "IMPOSSIBLE"
    
    # Topological sort using Kahn's algorithm
    from collections import deque
    
    queue = deque([char for char in range(ord('a'), ord(L) + 1) if in_degree[char] == 0])
    topo_order = []
    
    while queue:
        if len(queue) > 1:
            return "AMBIGUOUS"
        
        char = queue.popleft()
        topo_order.append(chr(char))
        
        for neighbor in graph[chr(char)]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(topo_order) == (ord(L) - ord('a') + 1):
        return ''.join(topo_order)
    else:
        return "IMPOSSIBLE"

# Read input
L, N = map(str, input().split())
words = [input() for _ in range(int(N))]

# Output the result
print(find_alphabet_order(L, words))