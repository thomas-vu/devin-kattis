def longest_mountainous_palindromic_subarray(arr):
    n = len(arr)
    if n < 3:
        return -1
    
    # Find all mountain ranges
    mountains = []
    for i in range(1, n - 1):
        if arr[i-1] < arr[i] > arr[i+1]:
            left = i - 1
            right = i + 1
            while left > 0 and arr[left-1] < arr[left]:
                left -= 1
            while right < n - 1 and arr[right+1] < arr[right]:
                right += 1
            mountains.append((left, right))
    
    # Find the longest mountain that is also a palindrome
    max_length = -1
    for start, end in mountains:
        if is_palindrome(arr[start:end+1]):
            max_length = max(max_length, end - start + 1)
    
    return max_length if max_length != -1 else -1

def is_palindrome(subarr):
    return subarr == subarr[::-1]

# Read input
n = int(input())
arr = [int(input()) for _ in range(n)]

# Output the result
print(longest_mountainous_palindromic_subarray(arr))