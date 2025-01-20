def can_form_perfect_team(c, edges, players):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    player_info = {}
    for i in range(10):
        name, country, league, team = players[i].split()
        player_info[i] = (country, league, team)
    
    synergy = [[0] * 10 for _ in range(10)]
    
    for i in range(10):
        for j in graph[i]:
            synergy_ij = 0
            if player_info[i][0] == player_info[j][0]:
                synergy_ij += 1
            if player_info[i][1] == player_info[j][1]:
                synergy_ij += 1
            if player_info[i][2] == player_info[j][2]:
                synergy_ij += 2
            if player_info[i][0] == player_info[j][0] and player_info[i][1] == player_info[j][1]:
                synergy_ij += 1
            if player_info[i][0] == player_info[j][0] and player_info[i][2] == player_info[j][2]:
                synergy_ij += 2
            synergy[i][j] = synergy_ij
            synergy[j][i] = synergy_ij
    
    degrees = [len(graph[i]) for i in range(10)]
    
    def bfs(start):
        visited = [False] * 10
        queue = deque([start])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return sum(visited) == 10
    
    for i in range(10):
        if degrees[i] > sum(synergy[i]):
            return "no"
    return "yes"

# Read input
c = int(input())
edges = [tuple(map(int, input().split())) for _ in range(c)]
players = [input() for _ in range(10)]

# Output the result
print(can_form_perfect_team(c, edges, players))