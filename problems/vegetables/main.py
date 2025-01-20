def min_cuts(T, N, weights):
    low = 0
    high = max(weights)
    
    while low < high:
        mid = (low + high) // 2
        
        # Count the number of cuts needed for a mid value
        cuts = sum((w - 1) // mid for w in weights)
        
        if cuts > (N * (1 / T - 1)):
            high = mid
        else:
            low = mid + 1
    
    return low - 1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = float(data[index])
    N = int(data[index + 1])
    weights = [int(data[i]) for i in range(index + 2, index + 2 + N)]
    
    result = min_cuts(T, N, weights)
    print(result)

if __name__ == "__main__":
    main()