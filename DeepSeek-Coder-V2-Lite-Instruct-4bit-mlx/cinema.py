N, M = map(int, input().split())
groups = list(map(int, input().split()))

accepted_count = 0
for group in groups:
    if N - group >= 0:
        N -= group
        accepted_count += 1
    else:
        break

print(M - accepted_count)