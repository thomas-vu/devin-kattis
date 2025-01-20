def find_longest_trade(n, trades):
    graph = {}
    for trade in trades:
        name, has, wants = trade.split()
        graph[name] = (has, wants)
    
    def dfs(node, visited):
        if node in visited:
            return 0
        visited.add(node)
        has, wants = graph[node]
        length = 1
        if has in graph and wants not in visited:
            length += dfs(wants, visited)
        if wants in graph and has not in visited:
            length += dfs(has, visited)
        return length
    
    longest_trade = 0
    for person in graph:
        visited = set()
        trade_length = dfs(person, visited)
        if trade_length > longest_trade:
            longest_trade = trade_length
    
    return longest_trade if longest_trade > 1 else "No trades possible"

n = int(input())
trades = [input().strip() for _ in range(n)]
print(find_longest_trade(n, trades))