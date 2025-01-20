def is_possible(n, m, initial_labels, test_sequence):
    from itertools import permutations
    
    # Generate all possible rotations of the initial labeling
    rotations = [initial_labels[i:] + initial_labels[:i] for i in range(n)]
    
    # Generate all possible reflections of the initial labeling
    reflections = [list(reversed(rot)) for rot in rotations]
    
    # Combine rotations and reflections into dihedral group actions
    dihedral_actions = rotations + reflections
    
    # Convert the test sequence into a list of tuples for easy comparison
    test_sequence = [(test_sequence[i], test_sequence[i+1]) for i in range(m-1)]
    
    # Check if any dihedral action results in the test sequence
    for action in dihedral_actions:
        # Convert the current labeling into a list of tuples and compare with test sequence
        current_sequence = [(action[i], action[(i+1)%n]) for i in range(n)]
        if current_sequence == test_sequence:
            return 1
    return 0

# Read input
n, m = map(int, input().split())
initial_labels = list(map(int, input().split()))
test_sequence = list(map(int, input().split()))

# Output the result of the check
print(is_possible(n, m, initial_labels, test_sequence))