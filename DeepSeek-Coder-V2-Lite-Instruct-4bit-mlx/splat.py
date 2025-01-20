def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    c = int(data[index])
    index += 1
    
    paintings = []
    
    for _ in range(c):
        n = int(data[index])
        index += 1
        drops = []
        for _ in range(n):
            X = float(data[index])
            Y = float(data[index + 1])
            V = float(data[index + 2])
            color = data[index + 3]
            index += 4
            drops.append(((X, Y), V, color))
        
        paintings.append(drops)
    
    m = int(data[index])
    index += 1
    queries = []
    for _ in range(m):
        X = float(data[index])
        Y = float(data[index + 1])
        index += 2
        queries.append((X, Y))
    
    # Process each painting and store the final colors at each point
    canvas_colors = {}
    
    for drops in paintings:
        for (x, y), v, color in drops:
            radius = int(v ** 0.5)
            for dx in range(-radius, radius + 1):
                for dy in range(-radius, radius + 1):
                    if dx**2 + dy**2 <= radius**2:
                        point = (x + dx, y + dy)
                        canvas_colors[point] = color
    
    # Answer the queries based on the final colors
    for query in queries:
        if query in canvas_colors:
            print(canvas_colors[query])
        else:
            print("white")

if __name__ == "__main__":
    main()