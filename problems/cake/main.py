def main():
    p, q, n = map(int, input().split())
    roses = [tuple(map(int, input().split())) for _ in range(n)]
    
    # Create a list to store the cuts for each person
    cuts = []
    
    # Find the minimum and maximum x and y coordinates of the roses
    min_x = 1
    max_x = p
    min_y = 1
    max_y = q
    
    for x, y in roses:
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)
    
    # Add the cuts for each person
    for x, y in roses:
        a = min(x, min_x)
        b = min(y, min_y)
        c = max(x, max_x)
        d = max(y, max_y)
        cuts.append((a, b, c, d))
    
    # Output the cuts for each person
    for cut in cuts:
        print(*cut)
    
    # Calculate the area of the leftovers
    leftover_area = (max_x - min_x + 1) * (max_y - min_y + 1)
    for x, y in roses:
        leftover_area -= (max(x, min_x) - min(x, max_x) + 1) * (max(y, min_y) - min(y, max_y) + 1)
    
    # Output the area of the leftovers
    print(leftover_area)

if __name__ == "__main__":
    main()