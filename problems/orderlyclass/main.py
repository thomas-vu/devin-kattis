def count_reversals(A, B):
    n = len(A)
    # Create a list to store the positions of each character in A
    pos_A = {char: [] for char in set(A)}
    for i, char in enumerate(A):
        pos_A[char].append(i)
    
    # Create a list to store the positions of each character in B
    pos_B = {char: [] for char in set(B)}
    for i, char in enumerate(B):
        pos_B[char].append(i)
    
    # Check if the positions are compatible for each character
    for char in pos_A:
        if pos_A[char] != pos_B[char]:
            return 0
    
    # Calculate the number of ways to reverse consecutive groups in A to form B
    count = 1
    i = 0
    while i < n:
        j = i
        while j < n and A[i] == A[j]:
            j += 1
        # The number of ways to reverse the subarray from i to j-1 is (j-i)//2
        count *= ((j - i) // 2 + 1)
        i = j
    return count

# Read input
import sys
input = sys.stdin.read
data = input().split()
A = data[0]
B = data[1]

# Output the result
print(count_reversals(A, B))