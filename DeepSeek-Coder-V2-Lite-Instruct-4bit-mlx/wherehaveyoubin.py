def min_cost_to_move_bins(n, bins, deletions, additions):
    # Convert the initial usage of bins to a list for easier manipulation
    bin_list = list(bins)
    
    # Process deletions
    for del_bin in deletions:
        bin_list[del_bin - 1] = 'X'
    
    # Process additions
    for add_bin, company in additions:
        bin_list[add_bin - 1] = company
    
    # Initialize costs and current companies positions
    cost = 0
    i = 0
    
    while i < n:
        if bin_list[i] != 'X':
            company = bin_list[i]
            j = i + 1
            while j < n and bin_list[j] == company:
                j += 1
            # Calculate the cost to move items from i to j-1 bins of company to a new position
            total_items = sum(bins[k] for k in range(i, j))
            cost += total_items
            i = j
        else:
            i += 1
    
    return cost

# Read input
n = int(input().strip())
bins = list(map(int, input().strip().split()))
d = int(input().strip())
deletions = list(map(int, input().strip().split()))
additions_input = input().strip()
if additions_input == '0':
    additions = []
else:
    additions = [(i + 1, char) for i, char in enumerate(additions_input)]

# Calculate and print the minimal cost
print(min_cost_to_move_bins(n, bins, deletions, additions))