import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    N = int(input())
    computers = [tuple(map(int, input().split())) for _ in range(N)]
    
    total_distance = 0.0
    
    for i in range(N):
        for j in range(i + 1, N):
            distance = calculate_distance(*computers[i], *computers[j])
            total_distance += distance
    
    print("{:.6f}".format(total_distance))

if __name__ == "__main__":
    main()