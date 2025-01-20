N = int(input())
a_i = []
b_i = []
for _ in range(N):
    a, b = map(int, input().split())
    a_i.append(a)
    b_i.append(b)

total_players = sum(a_i)
total_umpires = sum(b_i)

# The number of possible matches is the product of the number of players and umpires
matches = total_players * total_umpires - N * (N - 1) // 2
print(matches)