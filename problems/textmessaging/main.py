def min_keypresses(P, K, L, frequencies):
    # Sort the frequencies in descending order
    sorted_frequencies = sorted(frequencies, reverse=True)
    
    # Calculate the total key presses for each key
    total_presses = 0
    for i in range(L):
        # The number of presses required to type the ith most frequent letter
        presses = sorted_frequencies[i] * ((i // P) + 1)
        total_presses += presses
    
    return total_presses

# Read the number of test cases
N = int(input())
for case_number in range(1, N + 1):
    # Read the parameters for each test case
    P, K, L = map(int, input().split())
    frequencies = list(map(int, input().split()))
    
    # Calculate the minimum number of key presses
    result = min_keypresses(P, K, L, frequencies)
    
    # Output the result for each test case
    print(f"Case #{case_number}: {result}")