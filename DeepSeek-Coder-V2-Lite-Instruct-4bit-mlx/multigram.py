def is_multigram(word):
    n = len(word)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            root = word[:i]
            rest = word[i:]
            if sorted(root) == sorted(rest):
                return root
    return -1

word = input().strip()
result = is_multigram(word)
print(result)