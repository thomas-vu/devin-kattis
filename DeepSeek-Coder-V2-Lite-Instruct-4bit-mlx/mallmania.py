def distance(a1, s1, a2, s2):
    return abs(a1 - a2) + abs(s1 - s2)

def min_crossing_distance(mall1, mall2):
    min_dist = float('inf')
    for (a1, s1) in mall1:
        for (a2, s2) in mall2:
            min_dist = min(min_dist, distance(a1, s1, a2, s2))
    return min_dist

def parse_mall(perimeter, lines):
    mall = []
    for i in range(perimeter):
        a, s = map(int, lines[i].split())
        mall.append((a, s))
    return mall

def main():
    while True:
        perimeter1 = int(input())
        if perimeter1 == 0:
            break
        lines1 = [input() for _ in range(perimeter1)]
        mall1 = parse_mall(perimeter1, lines1)
        
        perimeter2 = int(input())
        if perimeter2 == 0:
            break
        lines2 = [input() for _ in range(perimeter2)]
        mall2 = parse_mall(perimeter2, lines2)
        
        print(min_crossing_distance(mall1, mall2))

if __name__ == "__main__":
    main()