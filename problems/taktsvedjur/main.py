n = int(input())
scores = [int(input()) for _ in range(n)]

multiplier = 1
total_score = 0
for score in scores:
    if score > 0:
        total_score += score * multiplier
        multiplier *= 2 if score > 0 else 1
    else:
        multiplier = max(multiplier // 2, 1)

print(total_score)