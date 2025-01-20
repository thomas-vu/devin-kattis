def find_pivot(arr):
    min_val = float('inf')
    max_val = float('-inf')
    
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return min_val, max_val

n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print("0")
else:
    min_val, max_val = find_pivot(arr)
    
    if min_val == arr[0] and max_val == arr[-1]:
        print("1")
        print(arr[0])
    else:
        print("0")