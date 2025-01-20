n, s = map(int, input().split())
participants = {}
for _ in range(n):
    t, b = input().split()
    participants[t] = int(b)

winning_groups = set()
for i in range(2**n):
    sum_bets = 0
    for j in range(n):
        if i & (1 << j):
            sum_bets += participants[list(participants.keys())[j]]
    if sum_bets == s:
        winning_groups.add(i)

winners = []
for i in range(n):
    if (1 << i) & winning_groups:
        winners.append(list(participants.keys())[i])

print(len(winners))
for winner in winners:
    print(winner)