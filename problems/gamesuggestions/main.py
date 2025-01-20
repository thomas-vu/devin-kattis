def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    F = int(data[0])
    S = int(data[1])
    C = int(data[2])
    
    friends_suggestions = []
    for i in range(F):
        index = 3 + (i * S)
        friends_suggestions.append(data[index: index + S])
    
    categories = {}
    for i in range(C):
        index = 3 + F * S + (i * (2 + int(data[3 + F * S + i * 2])))
        cat_name = data[index]
        num_suggestions = int(data[index + 1])
        suggestions = data[index + 2: index + 2 + num_suggestions]
        categories[cat_name] = suggestions
    
    # Create a graph where friends are nodes and edges represent possible suggestions
    from collections import defaultdict
    
    graph = defaultdict(list)
    for fs in friends_suggestions:
        for s1 in fs:
            graph[s1].extend(fs)
    
    # Use bipartite matching to find the maximum matching in the graph
    match = {}
    def dfs(node, visited):
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                if match.get(neighbour, None) is None or dfs(match[neighbour], visited):
                    match[neighbour] = node
                    return True
        return False
    
    for cat, suggestions in categories.items():
        visited = set()
        for suggestion in suggestions:
            if dfs(suggestion, visited):
                break
    
    max_suggestions = len(match)
    print(max_suggestions)

if __name__ == "__main__":
    main()