import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def min_lines(n, d, places):
    stations = []
    for place in places:
        if distance(0, 0, place[0], place[1]) <= d:
            stations.append((place[0], place[1]))
    
    if not stations:
        return 1
    
    count = len(stations)
    while True:
        new_stations = []
        for i in range(len(stations)):
            covered = False
            for j in range(i + 1, len(stations)):
                mid_x = (stations[i][0] + stations[j][0]) / 2
                mid_y = (stations[i][1] + stations[j][1]) / 2
                if distance(0, 0, mid_x, mid_y) <= d:
                    new_stations.append((mid_x, mid_y))
                    count -= 1
                    covered = True
            if not covered:
                new_stations.append(stations[i])
        stations = new_stations
        if not stations:
            break
    return count

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        n = int(data[index])
        d = float(data[index + 1])
        index += 2
        places = []
        for _ in range(n):
            x = int(data[index])
            y = int(data[index + 1])
            places.append((x, y))
            index += 2
        results.append(min_lines(n, d, places))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()