def find_shortest_string(k):
    # Helper function to generate the next character in the sequence
    def next_char(c):
        return chr(ord(c) + 1)
    
    # Start with the smallest character 'a'
    current_char = 'a'
    
    # Initialize the string and the sum of differences
    result_string = ''
    total_sum = 0
    
    # Build the string by adding consecutive characters and updating the sum of differences
    while total_sum < k:
        next_char_value = ord(current_char) - ord('a') + 1
        if total_sum + next_char_value <= k:
            result_string += current_char
            total_sum += next_char_value
        else:
            break
        current_char = next_char(current_char)
    
    # Adjust the string to match the exact sum required by subtracting from the last character
    while total_sum > k:
        if ord(result_string[-1]) - ord('a') + 1 > 1:
            total_sum -= (ord(result_string[-1]) - ord('a') + 1)
            result_string = result_string[:-1]
    
    return result_string

# Read input from stdin
import sys
for line in sys.stdin:
    k = int(line.strip())
    result = find_shortest_string(k)
    print(result)