def count_favourable_stories(sections):
    graph = {i: [] for i in range(1, 401)}
    favourable_ends = set()
    
    for section in sections:
        page, choice1, choice2, choice3 = section[0], section[1], section[2], section[3]
        graph[page] = [choice1, choice2, choice3]
    
    def dfs(node, visited):
        if node in favourable_ends:
            return 1
        count = 0
        for choice in graph[node]:
            if choice not in visited:
                visited.add(choice)
                count += dfs(choice, visited)
        return count
    
    for section in sections:
        if section[4] == 'favourably':
            favourable_ends.add(section[0])
    
    visited = set()
    visited.add(1)
    return dfs(1, visited)

def main():
    T = int(input())
    results = []
    for _ in range(T):
        S = int(input())
        sections = []
        for _ in range(S):
            section_info = list(map(int, input().split())) if input().strip() != 'favourably' and input().strip() != 'catastrophically' else list(input().split())
            if len(section_info) == 4:
                sections.append([*section_info, 'favourably'] if section_info[1] == section_info[2] or section_info[1] == section_info[3] or section_info[2] == section_info[3] else ['favourably'])
            elif len(section_info) == 1:
                sections.append([*section_info, 'catastrophically'])
        results.append(count_favourable_stories(sections))
    for result in results:
        print(result)

main()