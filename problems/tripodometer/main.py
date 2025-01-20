N = int(input())
distances = list(map(int, input().split()))
total_distance = sum(distances)
possible_totals = set()

for i in range(N):
    current_total = total_distance - distances[i]
    possible_totals.add(current_total)

print(len(possible_totals))
sorted_possible_totals = sorted(list(possible_totals))
for total in sorted_possible_totals:
    print(total, end=' ')