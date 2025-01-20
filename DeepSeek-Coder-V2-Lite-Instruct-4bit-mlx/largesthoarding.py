def max_revenue(skyscrapers):
    n = len(skyscrapers)
    max_area = 0
    
    for i in range(n):
        height_i = skyscrapers[i][0]
        width_i = skyscrapers[i][1]
        
        for j in range(i + 1, n):
            height_j = skyscrapers[j][0]
            width_j = skyscrapers[j][1]
            
            min_height = float('inf')
            for k in range(i, j + 1):
                min_height = min(min_height, skyscrapers[k][0])
            
            area = (j - i + 1) * min_height
            max_area = max(max_area, area)
    
    return max_area * 50

def main():
    n = int(input())
    skyscrapers = [list(map(int, input().split())) for _ in range(n)]
    result = max_revenue(skyscrapers)
    print(result)

if __name__ == "__main__":
    main()