import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def time_to_walk(distance):
    return distance / 10 * 60

def time_to_subway(distance):
    return distance / 40 * 60

def main():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    
    subway_lines = []
    while True:
        line = list(map(int, input().split()))
        if line[-2] == -1 and line[-1] == -1:
            break
        subway_lines.append(line)
    
    min_time = float('inf')
    
    for line in subway_lines:
        n = len(line) // 2
        for i in range(n):
            start_x, start_y = line[2*i], line[2*i+1]
            end_x, end_y = line[(2*i+2) % (2*n)], line[(2*i+3) % (2*n)]
            if start_x == -1 and start_y == -1:
                break
            walk_distance = distance(x1, y1, start_x, start_y)
            subway_distance = distance(start_x, start_y, end_x, end_y)
            walk_time = time_to_walk(walk_distance)
            subway_time = time_to_subway(subway_distance)
            next_walk_distance = distance(end_x, end_y, x2, y2)
            next_walk_time = time_to_walk(next_walk_distance)
            total_time = walk_time + subway_time + next_walk_time
            min_time = min(min_time, total_time)
    
    print(round(min_time))

if __name__ == "__main__":
    main()