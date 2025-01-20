def min_operations_to_sort(arr):
    operations = 0
    while True:
        sorted_flag = all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
        if sorted_flag:
            break
        
        min_val = min(arr)
        for i in range(len(arr)):
            if arr[i] == min_val:
                arr = arr[:i] + arr[i+1:] + [min_val]
                operations += 1
                break
    
    return operations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    P = int(data[0])
    index = 1
    results = []
    
    for _ in range(P):
        K = int(data[index])
        N = int(data[index + 1])
        arr = []
        for i in range(2, N + 2):
            row = list(map(int, data[i].split()))
            arr.extend(row)
        
        operations = min_operations_to_sort(arr)
        results.append((K, operations))
        index += N + 2
    
    for result in results:
        print(f"{result[0]} {result[1]}")

if __name__ == "__main__":
    main()