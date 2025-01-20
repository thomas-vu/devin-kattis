import sys

def find_real_gold_stack(n):
    low = 1
    high = n

    while low <= high:
        mid = (low + high) // 2
        # Ask how many coins from each stack in the range [low, mid]
        print(f"? {' '.join(['10' for _ in range(low, mid + 1)])}")
        sys.stdout.flush()
        
        # Read the response from the scale
        total_weight = int(input())
        
        # Calculate the expected weight if all coins were counterfeit
        expected_weight = (mid - low + 1) * n
        
        # If the total weight is less than expected, real gold coins are in the lower half
        if total_weight < expected_weight:
            high = mid - 1
        # If the total weight is more than expected, real gold coins are in the upper half
        else:
            low = mid + 1
    
    # The real gold stack is at the position where the scale would be balanced
    return low - 1

# Read the number of stacks from the input
n = int(input())

# Find and output the stack containing real gold coins
real_gold_stack = find_real_gold_stack(n)
print(f"! {real_gold_stack}")