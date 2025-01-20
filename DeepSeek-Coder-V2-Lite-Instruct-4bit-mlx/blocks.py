def count_figures(n):
    if n == 1:
        return 0
    elif n % 2 == 1:
        return count_figures(n - 1) + (n * n - (n - 1) * (n - 1)) // 2
    else:
        return count_figures(n - 1) + (n * n - (n - 2) * (n - 2)) // 2

def main():
    t = int(input())
    for i in range(1, t + 1):
        n = int(input())
        result = count_figures(n) % 10000
        print(f"Case {i}: {result}")

if __name__ == "__main__":
    main()