import sys

def calculate_time(x, y):
    return ((x - 0) ** 2 + y ** 2) ** 0.5

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        
        houses = []
        for _ in range(n):
            x, y = map(float, input().split())
            houses.append((x, y))
        
        min_time = float('inf')
        best_x = 0.0
        
        for x in range(n):
            max_distance = 0.0
            for y in range(n):
                distance = calculate_time(houses[x][0], houses[y][1])
                if distance > max_distance:
                    max_distance = distance
            if max_distance < min_time:
                min_time = max_distance
                best_x = houses[x][0]
        
        print(f"{best_x:.12f} {min_time:.12f}")

if __name__ == "__main__":
    main()