def calculate_privacy(x1, y1, stands):
    min_distance = float('inf')
    for x2, y2 in stands:
        distance = abs(x1 - x2) + abs(y1 - y2)
        if distance < min_distance:
            min_distance = distance
    return min_distance

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    test_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(test_cases):
        n, w, h = map(int, data[index].split())
        index += 1
        stands = []
        for i in range(n):
            x, y = map(int, data[index].split())
            stands.append((x, y))
            index += 1
        
        max_privacy = 0
        for i in range(w):
            for j in range(h):
                privacy_barack = calculate_privacy(i, j, stands)
                privacy_mitt = calculate_privacy(i, j, stands)
                min_privacy = min(privacy_barack, privacy_mitt)
                if min_privacy > max_privacy:
                    max_privacy = min_privacy
        
        results.append(max_privacy)
    
    for result in results:
        print(result)

main()