def hamming_distance(word1, word2):
    return sum(c1 != c2 for c1, c2 in zip(word1, word2))

def count_points_in_ellipse(q, n, D, f1, f2):
    count = 0
    for i in range(q**n):
        word = format(i, f'0{n}b')
        dist1 = hamming_distance(f1, word)
        dist2 = hamming_distance(f2, word)
        if dist1 + dist2 == D:
            count += 1
    return count

q, n, D = map(int, input().split())
f1 = input()
f2 = input()
print(count_points_in_ellipse(q, n, D, f1, f2))