n, k, d = map(int, input().split())
friends = [int(input()) for _ in range(n)]

count = 0
for friend_day in friends:
    if friend_day + 14 >= k:
        count += 1

print(count)