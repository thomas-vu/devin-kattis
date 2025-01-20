def count_shandies(B, L):
    # Each shandy requires 1 bottle of beer and 1 bottle of lemonade.
    total_shandies = min(B, L) * 2
    return total_shandies

# Read input from stdin
import sys
input = sys.stdin.readlines()
B = int(input[0].strip())
L = int(input[1].strip())

# Calculate and print the number of shandies
print(count_shandies(B, L))