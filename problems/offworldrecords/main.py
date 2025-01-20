n, c, p = map(int, input().split())
records = [int(input()) for _ in range(n)]

count = 0
current_record = c
previous_record = p

for height in records:
    if height > current_record + previous_record:
        count += 1
        previous_record = current_record
        current_record = height
    else:
        previous_record = max(previous_record, height)

print(count)