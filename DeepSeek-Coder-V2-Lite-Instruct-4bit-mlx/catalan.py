def catalan_number(n):
    if n <= 1:
        return 1
    cat = [0] * (n + 1)
    cat[0], cat[1] = 1, 1
    for i in range(2, n + 1):
        cat[i] = sum(cat[j] * cat[i - j - 1] for j in range(i))
    return cat[n]

def main():
    q = int(input())
    for _ in range(q):
        x = int(input())
        print(catalan_number(x))

main()