n, k = map(int, input().split())
words = ""
i = 1
while len(words) < n:
    words += str(i)
    i += 1
count = 0
for word in words[:n]:
    if int(word) % k == 0:
        count += 1
print(count)