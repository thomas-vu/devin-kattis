def frequency_sort(N, C, message):
    from collections import Counter
    
    # Count the frequency of each number in the message
    freq = Counter(message)
    
    # Sort the message based on frequency and then by value
    sorted_message = sorted(message, key=lambda x: (freq[x], message.index(x)))
    
    return sorted_message

# Read input from stdin
N, C = map(int, input().split())
message = list(map(int, input().split()))

# Get the sorted message
sorted_message = frequency_sort(N, C, message)

# Print the sorted message
print(' '.join(map(str, sorted_message)))