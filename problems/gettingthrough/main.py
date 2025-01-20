def can_pass(w, sensors):
    left = 0.0
    right = min([sensor[2] + sensor[1] for sensor in sensors])
    
    while right - left > 1e-6:
        mid = (left + right) / 2.0
        min_x = float('inf')
        max_x = -float('inf')
        
        for x, y, r in sensors:
            if mid <= r:
                continue
            dx = (mid**2 - r**2 + y**2)**0.5
            min_x = min(min_x, x - dx)
            max_x = max(max_x, x + dx)
        
        if min_x <= 0 and max_x >= w:
            left = mid
        else:
            right = mid
    
    return left if left > 0 else 0.0

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    test_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(test_cases):
        w = int(data[index])
        index += 1
        n = int(data[index])
        index += 1
        sensors = []
        for _ in range(n):
            x = int(data[index])
            y = int(data[index + 1])
            r = int(data[index + 2])
            index += 3
            sensors.append((x, y, r))
        results.append(can_pass(w, sensors))
    
    for result in results:
        print("{:.6f}".format(result))

if __name__ == "__main__":
    main()