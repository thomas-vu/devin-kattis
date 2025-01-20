def main():
    N = int(input())
    words = [input() for _ in range(N)]
    for i in range(1, N + 1):
        if i % 2 == 1:
            print(words[i - 1])

if __name__ == "__main__":
    main()