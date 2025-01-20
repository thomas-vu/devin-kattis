def is_safe(queens):
    for i in range(len(queens)):
        for j in range(i + 1, len(queens)):
            if queens[i][0] == queens[j][0] or queens[i][1] == queens[j][1] or abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return "INCORRECT"
    return "CORRECT"

def main():
    N = int(input())
    queens = [tuple(map(int, input().split())) for _ in range(N)]
    result = is_safe(queens)
    print(result)

if __name__ == "__main__":
    main()