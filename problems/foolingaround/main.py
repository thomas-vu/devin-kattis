def who_wins(N):
    if N == 1 or (N > 2 and N % 2 != 0):
        return "Alice"
    else:
        return "Bob"

def main():
    Q = int(input())
    for _ in range(Q):
        N = int(input())
        winner = who_wins(N)
        print(winner)

if __name__ == "__main__":
    main()