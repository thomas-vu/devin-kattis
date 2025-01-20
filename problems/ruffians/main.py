def find_pair(grid1, grid2):
    for num in grid1:
        if num in grid2:
            return "YES"
    return "NO"

def main():
    t = int(input())
    for _ in range(t):
        grid1 = list(map(int, input().split()))
        grid2 = list(map(int, input().split()))
        result = find_pair(grid1, grid2)
        print(result)

if __name__ == "__main__":
    main()