def find_pattern(s):
    n = len(s)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            pattern = s[:i]
            repeated_count = n // i
            if pattern * repeated_count == s:
                return i
    return n

def main():
    n = int(input())
    for _ in range(n):
        s = input().strip()
        print(find_pattern(s))

if __name__ == "__main__":
    main()