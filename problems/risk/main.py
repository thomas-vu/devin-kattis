def read_ints():
    return list(map(int, input().split()))

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        armies = read_ints()
        borders = [list(input().strip()) for _ in range(n)]
        
        min_weakest = float('inf')
        for i in range(n):
            if armies[i] > 0:
                weak_count = sum(1 for j in range(n) if borders[i][j] == 'Y' and armies[j] > 0)
                min_weakest = min(min_weakest, weak_count)
        
        print(min_weakest if min_weakest != float('inf') else 0)

if __name__ == "__main__":
    main()