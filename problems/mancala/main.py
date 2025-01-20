def find_winnable_board(N):
    board = [0] * (2*N + 1)
    board[0] = N
    for i in range(1, N+1):
        board[i] = (N // i) * i
    return board

def main():
    P = int(input())
    for _ in range(P):
        K, N = map(int, input().split())
        board = find_winnable_board(N)
        bins = [str(board[i]) for i in range(1, N+1)]
        print(K, board[N])
        for i in range(0, len(bins), 10):
            print(' '.join(bins[i:i+10]))

if __name__ == "__main__":
    main()