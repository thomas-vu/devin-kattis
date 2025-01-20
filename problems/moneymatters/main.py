def can_balance_debts(n, debts, friendships):
    # Create adjacency list for friends graph
    adj_list = [[] for _ in range(n)]
    for x, y in friendships:
        adj_list[x].append(y)
        adj_list[y].append(x)
    
    # Create a list to store the net balance of each person after debts are settled
    balances = [0] * n
    
    def dfs(node, visited):
        if node in visited:
            return
        visited.add(node)
        for friend in adj_list[node]:
            balances[friend] += balances[node]
            dfs(friend, visited)
    
    # Initialize the net balance of each person based on debts
    for i in range(n):
        balances[i] = debts[i]
    
    # Perform a DFS to propagate the net balance through friendships
    visited = set()
    for i in range(n):
        if i not in visited:
            dfs(i, visited)
    
    # Check if all balances are zero (possible to balance debts)
    return "POSSIBLE" if all(balance == 0 for balance in balances) else "IMPOSSIBLE"

# Read input
n, m = map(int, input().split())
debts = [int(input()) for _ in range(n)]
friendships = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

# Output the result
print(can_balance_debts(n, debts, friendships))