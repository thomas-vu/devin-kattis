K = int(input())
a = int(input())
b = int(input())

combinations = []
for kills in range(K // a + 1):
    for assists in range(K // b + 1):
        if kills * a + assists * b == K:
            combinations.append((kills, assists))

print(len(combinations))
for combo in combinations:
    print(*combo)