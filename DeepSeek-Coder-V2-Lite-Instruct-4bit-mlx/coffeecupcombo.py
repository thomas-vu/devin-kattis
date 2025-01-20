n = int(input())
s = input()

max_count = 0
current_count = 0
for i in range(n):
    if s[i] == '1':
        current_count += 1
        max_count = max(max_count, current_count)
    else:
        current_count = 0

if max_count == 0 and '1' in s:
    max_count = 1

print(max_count)