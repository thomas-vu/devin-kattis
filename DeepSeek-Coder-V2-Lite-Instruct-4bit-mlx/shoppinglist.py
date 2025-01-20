def find_common_items():
    n, m = map(int, input().split())
    lists = [input().split() for _ in range(n)]
    
    # Convert each list of items to a set to remove duplicates within each list
    sets = [set(lst) for lst in lists]
    
    # Find the intersection of all sets to get common items
    common_items = set.intersection(*sets)
    
    # Convert the result back to a sorted list before outputting
    common_items = sorted(common_items)
    
    # Output the number of common items followed by each item on a new line
    print(len(common_items))
    for item in common_items:
        print(item)

find_common_items()