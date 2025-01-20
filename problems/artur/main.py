def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    sticks = []
    for i in range(1, N + 1):
        x1, y1, x2, y2 = map(int, data[i].split())
        sticks.append(((x1, y1), (x2, y2)))
    
    # Calculate the distance of each stick from the x-axis
    distances = [(i + 1, min(y1, y2)) for i, ((x1, y1), (x2, y2)) in enumerate(sticks)]
    
    # Sort sticks by their distance from the x-axis
    distances.sort(key=lambda x: x[1])
    
    # Extract the sorted order of stick labels
    result = [d[0] for d in distances]
    
    # Output the result
    print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()