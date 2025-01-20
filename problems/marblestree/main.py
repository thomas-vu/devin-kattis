def min_moves(n, tree):
    def dfs(v, parent):
        moves = 0
        for child in tree[v]:
            if child != parent:
                moves += dfs(child, v)
        excess = marbles[v] - 1
        moves += abs(excess)
        return moves + excess
    
    for case in range(n):
        n, marbles = 0, []
        tree = {}
        for _ in range(n):
            line = list(map(int, input().split()))
            v, m, d = line[0], line[1], line[2:]
            marbles.append(m)
            tree[v] = d
        if n == 0:
            break
        result = dfs(1, -1)
        print(result)