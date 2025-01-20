MOD = 10**9 + 9

def count_unsorted(n, arr):
    # Create a list to track the position of each element in the original array
    pos = [0] * n
    for i, val in enumerate(arr):
        pos[val] = i
    
    # Create a BIT (Binary Indexed Tree) to count inversions
    bit = [0] * n
    
    def query(x):
        res = 0
        while x > 0:
            res += bit[x - 1]
            x -= x & -x
        return res
    
    def update(x, val):
        while x <= n:
            bit[x - 1] += val
            x += x & -x
    
    # Count the number of inversions using BIT
    inv_count = 0
    for i in range(n):
        update(i + 1, 1)
        inv_count += query(n) - query(pos[i])
    
    # Calculate the number of entirely unsorted sequences
    if inv_count == n * (n - 1) // 2:
        result = factorial(n)
    else:
        result = 0
    
    return result % MOD

def factorial(n):
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD
    return fact[n]

# Read input
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Output the result
print(count_unsorted(n, arr))