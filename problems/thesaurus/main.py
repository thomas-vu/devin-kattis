def find_minimum_length(N, M, essay, synonyms):
    # Create a graph to represent the synonym relationships
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for a, b in synonyms:
        graph[a].append(b)
        graph[b].append(a)
    
    # Find the shortest synonym for each word in the essay
    synonym_map = {}
    
    def bfs(start):
        visited = set()
        queue = deque([start])
        while queue:
            word = queue.popleft()
            if word not in visited:
                visited.add(word)
                for synonym in graph[word]:
                    if synonym not in visited:
                        queue.append(synonym)
        return list(visited)
    
    for word in essay:
        if word not in synonym_map:
            synonyms_of_word = bfs(word)
            for syn in synonyms_of_word:
                synonym_map[syn] = word
    
    # Calculate the minimum length of the essay after replacing words with their shortest synonyms
    min_length = 0
    for word in essay:
        min_length += len(synonym_map[word])
    
    return min_length

# Read input
N, M = map(int, input().split())
essay = list(input().split())
synonyms = [input().split() for _ in range(M)]

# Calculate and output the result
result = find_minimum_length(N, M, essay, synonyms)
print(result)