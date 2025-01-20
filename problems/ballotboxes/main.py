def solve(N, B, populations):
    low = 1
    high = sum(populations)
    
    while low < high:
        mid = (low + high) // 2
        boxes_needed = sum((pop + mid - 1) // mid for pop in populations)
        
        if boxes_needed > B:
            low = mid + 1
        else:
            high = mid
    
    return low

def main():
    while True:
        line = input()
        if line == "-1 -1":
            break
        
        N, B = map(int, line.split())
        populations = [int(input()) for _ in range(N)]
        
        result = solve(N, B, populations)
        print(result)

if __name__ == "__main__":
    main()