n = int(input())
words = [input().strip() for _ in range(n)]
pairs = set()

for i in range(n):
    for j in range(i + 1, n):
        word1 = words[i]
        word2 = words[j]
        diff_count = 0
        for k in range(len(word1)):
            if word1[k] != word2[k]:
                diff_count += 1
        if diff_count == 2:
            pairs.add((word1, word2))

print(len(pairs))