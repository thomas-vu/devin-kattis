def most_likely_outcome(N, M):
    # Create a dictionary to count the frequency of each possible sum
    sums_count = {}
    
    # Simulate rolling two dice and count the frequency of each sum
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            sum_of_dice = i + j
            if sum_of_dice in sums_count:
                sums_count[sum_of_dice] += 1
            else:
                sums_count[sum_of_dice] = 1
    
    # Find the most likely outcome (the maximum frequency)
    max_count = max(sums_count.values())
    
    # Collect the sums that have the maximum frequency
    most_likely_sums = [sum_ for sum_, count in sums_count.items() if count == max_count]
    
    # Sort the most likely sums and print them
    most_likely_sums.sort()
    for sum_ in most_likely_sums:
        print(sum_)

# Read input from stdin
N, M = map(int, input().split())
most_likely_outcome(N, M)