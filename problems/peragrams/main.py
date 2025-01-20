def min_removals_to_peragram(s):
    from collections import Counter
    
    # Count the frequency of each character in the string
    char_count = Counter(s)
    
    # Calculate the number of characters that need to be removed
    odd_counts = sum(1 for count in char_count.values() if count % 2 == 1)
    
    # The number of characters to remove is the number of odd counts minus 1, if any
    return max(odd_counts - 1, 0)

# Read input from stdin
s = input().strip()

# Output the result
print(min_removals_to_peragram(s))