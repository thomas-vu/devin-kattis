def can_still_win(results, n):
    points = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if results[i][j] == '1':
                points[i][i] += 1
                points[j][j] += 1
            elif results[i][j] == 'd':
                points[i][i] += 0.5
                points[j][j] += 0.5
            elif results[i][j] == '0':
                points[i][i] += 1
    
    max_points = max(max(row) for row in points)
    
    winners = []
    for i in range(n):
        if points[i][i] == max_points:
            winners.append(i + 1)
    
    return ' '.join(map(str, winners))

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        results = [list(input().strip()) for _ in range(n)]
        print(can_still_win(results, n))

if __name__ == "__main__":
    main()