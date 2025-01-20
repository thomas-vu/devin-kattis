n, d, w = map(int, input().split())
inscription = [input() for _ in range(n)]

lines = []
current_line = ""
for i in range(d):
    for j in range(n):
        if (i + j) % 2 == 0:
            current_line += inscription[j][i]
        else:
            current_line += inscription[j][i][::-1]
    lines.append(current_line)
    current_line = ""

count = 0
for line in lines:
    words = line.split('.')
    for word in words:
        if len(word) > w:
            count += 1
            word = word[w:] + '.'
        else:
            count += 1
print(count)