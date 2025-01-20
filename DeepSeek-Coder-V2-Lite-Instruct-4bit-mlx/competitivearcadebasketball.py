n, p, m = map(int, input().split())
players = {}
for _ in range(n):
    name = input()
    players[name] = 0

for _ in range(m):
    name, points = input().split()
    players[name] += int(points)

winners = [name for name, score in players.items() if score >= p]
if winners:
    for winner in winners:
        print(f"{winner} wins!")
else:
    print("No winner!")