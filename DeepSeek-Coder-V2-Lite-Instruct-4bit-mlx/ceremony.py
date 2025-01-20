def min_charges(blocks):
    max_height = 0
    for block in blocks:
        max_height = max(max_height, block)
    
    charges = 0
    for i in range(1, max_height + 1):
        current_charge = sum(block // i for block in blocks)
        charges = min(charges, current_charge) if charges else current_charge
    
    return charges

# Read input
n = int(input())
blocks = list(map(int, input().split()))

# Calculate and output the result
print(min_charges(blocks))