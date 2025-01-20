def calculate_perimeter(x1, y1, x2, y2):
    return 2 * (x2 - x1 + 1) + 2 * (y2 - y1 + 1)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    test_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(test_cases):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        grid = []
        for i in range(n):
            row = data[index]
            grid.append([c for c in row])
            index += 1
        
        perimeters = {}
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '.':
                    for x in range(i + 1, n + 1):
                        for y in range(j + 1, m + 1):
                            if grid[x - 1][y - 1] == '.':
                                perimeter = calculate_perimeter(i, j, x, y)
                                if perimeter not in perimeters:
                                    perimeters[perimeter] = 0
                                perimeters[perimeter] += 1
        
        sorted_perimeters = sorted(perimeters.items())
        for perimeter, count in sorted_perimeters:
            if count > 0:
                results.append(f"{count} x {perimeter}")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()