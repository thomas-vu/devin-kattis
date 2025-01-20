def count_subsequences(N, B, A):
    # Find the index of B in the sequence A
    median_index = A.index(B)
    
    # Initialize the count of subsequences with odd length and median B
    count = 0
    
    # Iterate over all possible lengths of subsequences
    for length in range(1, N + 1, 2):
        # Initialize the number of elements less than B and greater than B
        less_than_B = 0
        greater_than_B = 0
        
        # Iterate over all subsequences of the current length
        for start in range(N - length + 1):
            end = start + length - 1
            
            # Calculate the number of elements less than B and greater than B in the current subsequence
            for i in range(start, end + 1):
                if A[i] < B:
                    less_than_B += 1
                elif A[i] > B:
                    greater_than_B += 1
            
            # Check if the median of the subsequence is B
            if less_than_B == greater_than_B:
                count += 1
            
            # Reset the counts for the next subsequence
            less_than_B = 0
            greater_than_B = 0
    
    return count

# Read input from stdin
N, B = map(int, input().split())
A = list(map(int, input().split()))

# Calculate and print the result
print(count_subsequences(N, B, A))