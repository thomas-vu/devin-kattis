def count_pairs(n):
    pairs = 0
    for y in range(1, int(2 * n**0.5) + 1):
        if (2 * n - y) % (y - n) == 0:
            x = (2 * n - y) // (y - n)
            if x > 0 and x != y:
                pairs += 1
    return pairs

def main():
    while True:
        try:
            line = input().strip()
            n = int(line.split('/')[1])
            print(count_pairs(n))
        except EOFError:
            break

if __name__ == "__main__":
    main()