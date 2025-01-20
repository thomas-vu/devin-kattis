def last_three_digits(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (3 * b + 2 * a) % 1000
    return f"{b:03d}"

def main():
    T = int(input())
    for t in range(1, T + 1):
        n = int(input())
        result = last_three_digits(n)
        print(f"Case #{t}: {result}")

if __name__ == "__main__":
    main()