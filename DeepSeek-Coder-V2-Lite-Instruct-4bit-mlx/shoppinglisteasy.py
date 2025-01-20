def find_common_items(lists):
    # Convert each list of items to a set for efficient comparison
    sets = [set(lst.split()) for lst in lists]
    
    # Find the intersection of all sets to get common items
    common_items = set.intersection(*sets)
    
    # Convert the result back to a sorted list of strings
    common_items = sorted(list(common_items))
    
    # Output the number of common items and then each item on a new line
    print(len(common_items))
    for item in common_items:
        print(item)

# Read input from stdin
n, m = map(int, input().split())
shopping_lists = [input() for _ in range(n)]

# Process and output the result
find_common_items(shopping_lists)