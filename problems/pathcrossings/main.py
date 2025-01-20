def euclidean_distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def main():
    from sys import stdin
    input = stdin.readline
    
    P, N = map(int, input().split())
    pings = []
    
    for _ in range(N):
        pi, xi, yi, ti = map(int, input().split())
        pings.append((pi, xi, yi, ti))
    
    player_pings = {}
    
    for pi, xi, yi, ti in pings:
        if pi not in player_pings:
            player_pings[pi] = []
        player_pings[pi].append((xi, yi, ti))
    
    crossed_paths = set()
    
    for pi in player_pings:
        pings_list = player_pings[pi]
        for i in range(len(pings_list)):
            for j in range(i + 1, len(pings_list)):
                x1, y1, t1 = pings_list[i]
                x2, y2, t2 = pings_list[j]
                if euclidean_distance(x1, y1, x2, y2) <= 1000 and abs(t1 - t2) <= 10:
                    crossed_paths.add((min(pi, pings_list[j][0]), max(pi, pings_list[j][0])))
    
    print(len(crossed_paths))
    for pair in sorted(crossed_paths):
        print(*pair)

if __name__ == "__main__":
    main()