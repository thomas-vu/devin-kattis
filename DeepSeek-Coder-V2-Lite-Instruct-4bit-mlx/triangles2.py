def calculate_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)

def main():
    N = int(input())
    seeds = [tuple(map(int, input().split())) for _ in range(N)]
    unique_triangles = set()
    
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                x1, y1 = seeds[i]
                x2, y2 = seeds[j]
                x3, y3 = seeds[k]
                
                area = calculate_area(x1, y1, x2, y2, x3, y3)
                if area > 0:
                    unique_triangles.add((i, j, k))
    
    total_cookies = 0
    for tri in unique_triangles:
        total_cookies += calculate_area(seeds[tri[0]][0], seeds[tri[0]][1], seeds[tri[1]][0], seeds[tri[1]][1], seeds[tri[2]][0], seeds[tri[2]][1]) ** 2
    
    print("{:.4f}".format(total_cookies))

if __name__ == "__main__":
    main()