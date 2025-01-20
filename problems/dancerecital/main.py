def min_quick_changes(routines):
    from collections import defaultdict
    
    # Create a dictionary to map each set of dancers to an index
    dancer_map = defaultdict(list)
    
    # Create a list to store the sets of dancers
    dancer_sets = []
    
    # Populate the lists with data from the routines
    for routine in routines:
        dance_set = set(routine)
        if dance_set not in dancer_sets:
            dancer_sets.append(dance_set)
        index = dancer_sets.index(dance_set)
        for dancer in dance_set:
            dancer_map[dancer].append(index)
    
    # Count the number of quick changes needed
    quick_changes = 0
    
    for i in range(len(dancer_sets) - 1):
        if dancer_map[list(dancer_map.keys())[i]][-1] > dancer_map[list(dancer_map.keys())[i + 1]][-1]:
            quick_changes += 1
    
    return quick_changes

# Main function to read input and output the result
def main():
    R = int(input())
    routines = [input() for _ in range(R)]
    result = min_quick_changes(routines)
    print(result)

if __name__ == "__main__":
    main()