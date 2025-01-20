def max_subarray_sum(arr, m):
    n = len(arr)
    max_sum = 0
    
    for i in range(n):
        if arr[i] == m:
            current_sum = 0
            for j in range(i, n):
                current_sum += arr[j]
                if arr[j] == m:
                    max_sum = max(max_sum, current_sum)
                if arr[j] < m:
                    break
    
    return max_sum

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    datasets = int(data[0])
    index = 1
    
    results = []
    for _ in range(datasets):
        n, m = int(data[index]), int(data[index + 1])
        arr = list(map(int, data[index + 2: index + 2 + n]))
        results.append(max_subarray_sum(arr, m))
        index += 2 + n
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()