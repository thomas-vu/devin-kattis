def is_champernowne_word(n):
    s = ""
    i = 1
    while len(s) < n:
        s += str(i)
        i += 1
    if len(s) == n:
        return i - 1
    else:
        return -1

n = int(input().strip())
print(is_champernowne_word(n))