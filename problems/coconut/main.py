def find_winner(s, n):
    players = [i for i in range(1, n + 1)]
    index = 0
    
    while len(players) > 1:
        index = (index + s - 1) % len(players)
        players.pop(index)
    
    return players[0]

# Read input from standard input
s, n = map(int, input().split())
print(find_winner(s, n))