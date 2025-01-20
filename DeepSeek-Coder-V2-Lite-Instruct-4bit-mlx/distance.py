def calculate_distance(s1, a1, s2, a2):
    return abs(s1 - s2) + abs(a1 - a2)

def main():
    N = int(input())
    trucks = [tuple(map(int, input().split())) for _ in range(N)]
    total_distance = 0
    
    for i in range(N):
        for j in range(i + 1, N):
            total_distance += calculate_distance(trucks[i][0], trucks[i][1], trucks[j][0], trucks[j][1])
    
    print(total_distance)

if __name__ == "__main__":
    main()