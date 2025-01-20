def find_spiral(x, y):
    # Directions in the order: right, up, left, down
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    direction_index = 0
    segment_length = 1
    segments = []
    
    while x != 0 or y != 0:
        if segment_length > abs(x) and segment_length > abs(y):
            return "NO PATH"
        
        if direction_index % 4 == 0:  # Right or Left
            steps = min(segment_length, abs(x))
            if x < 0:
                steps = -steps
            x += steps
        elif direction_index % 4 == 1:  # Up or Down
            steps = min(segment_length, abs(y))
            if y < 0:
                steps = -steps
            y += steps
        
        segments.append(segment_length)
        segment_length += 1
        direction_index += 1
    
    return segments

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    P = int(data[0])
    results = []
    
    for i in range(1, P + 1):
        x = int(data[i * 3 - 2])
        y = int(data[i * 3 - 1])
        
        result = find_spiral(x, y)
        if result == "NO PATH":
            results.append(f"{x} NO PATH")
        else:
            results.append(f"{x} {len(result)} {' '.join(map(str, result))}")
    
    for result in results:
        print(result)

main()