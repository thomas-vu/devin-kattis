def can_win(B, D, S):
    if B == 1 or D == 1:
        return S == 'Vicky'
    if S == 'Harry':
        return not can_win(B // 2, D, 'Vicky') or not can_win(B - B // 2, D, 'Vicky')
    else:
        return not can_win(B, D // 2, 'Harry') or not can_win(B, D - D // 2, 'Harry')

def main():
    N = int(input())
    for _ in range(N):
        B, D = map(int, input().split())
        S = input()
        if can_win(B, D, S):
            print(S + " can win")
        else:
            print(S + " cannot win")

if __name__ == "__main__":
    main()