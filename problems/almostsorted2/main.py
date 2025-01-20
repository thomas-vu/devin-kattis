def is_almost_sorted(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            temp = arr[:]
            temp[i:j+1] = reversed(temp[i:j+1])
            if is_sorted(temp):
                return "Yes"
    return "No"

def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True

# Read input
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Check if the array is almost sorted
result = is_almost_sorted(arr)
print(result)