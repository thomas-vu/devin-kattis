def can_win(n, moves):
    dp = [False] * (n + 1)
    for i in range(1, n + 1):
        for move in moves:
            if i >= move and not dp[i - move]:
                dp[i] = True
                break
    return dp[n]

def main():
    while True:
        try:
            line = input().split()
            n = int(line[0])
            m = int(line[1])
            moves = list(map(int, line[2:]))
            
            if can_win(n, moves):
                print("Stan wins")
            else:
                print("Ollie wins")
        except EOFError:
            break

if __name__ == "__main__":
    main()