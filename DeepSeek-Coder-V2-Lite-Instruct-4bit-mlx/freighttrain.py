def find_longest_luxembourg_train(N, W, L, wagons):
    left = 1
    right = N
    
    while left < right:
        mid = (left + right) // 2
        valid = True
        max_segment = 0
        
        for i in range(W):
            if wagons[i] <= mid:
                max_segment = max(max_segment, (wagons[i] - (mid - L + 1)) // mid)
            else:
                valid = False
                break
        
        if valid and max_segment <= L:
            right = mid
        else:
            left = mid + 1
    
    return left

def main():
    T = int(input())
    for _ in range(T):
        N, W, L = map(int, input().split())
        wagons = list(map(int, input().split()))
        result = find_longest_luxembourg_train(N, W, L, wagons)
        print(result)

if __name__ == "__main__":
    main()