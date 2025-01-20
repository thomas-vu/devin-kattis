N = int(input())
p_i = list(map(int, input().split()))
total_votes = sum(p_i)
max_losses = 0
for i in range(N):
    for j in range(i+1, N):
        if (p_i[i] + p_i[j]) < total_votes:
            max_losses = max(max_losses, p_i[i] + p_i[j])
print(max_losses)