def main():
    while True:
        line = input()
        if line == '-1':
            break
        
        a, b, c, m = map(int, line.split())
        chips = [tuple(map(int, input().split())) for _ in range(m)]
        
        # Sort chips by x, y, z to ensure they are in the correct order for slicing
        chips.sort()
        
        # Initialize parts with their respective coordinates
        parts = []
        for i in range(m):
            x, y, z = chips[i]
            parts.append((x, y, z, x, y, z))  # Each part is a single unit cube
        
        # Output the parts in the required format
        print('YES')
        for part in parts:
            print(f"{part[0]} {part[1]} {part[2]} {part[3]} {part[4]} {part[5]}")

if __name__ == "__main__":
    main()