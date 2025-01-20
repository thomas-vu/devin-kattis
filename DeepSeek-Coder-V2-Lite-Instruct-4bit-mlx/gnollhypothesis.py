def effective_spawn_chances(n, k, spawn_chances):
    # Normalize the spawn chances to sum up to 100%
    total_chance = sum(spawn_chances)
    normalized_chances = [chance / total_chance for chance in spawn_chances]
    
    # Initialize effective chances with zeros
    effective_chances = [0.0] * n
    
    # Simulate the spawn process k times for each spawn location
    for _ in range(k):
        # Choose a random set of k monster types with equal probability
        chosen_indices = [i for i in range(n)]  # All indices initially available
        while len(chosen_indices) > k:
            # Randomly select a pair of indices to merge
            idx1, idx2 = chosen_indices.pop(), chosen_indices.pop()
            # Add the spawn chances of the unselected types to the selected ones
            normalized_chances[idx1] += normalized_chances[idx2]
            # Remove the unselected type from consideration
            chosen_indices.append(idx1)
        
        # Assign the effective chances based on the chosen indices
        for idx in chosen_indices:
            effective_chances[idx] += normalized_chances[idx] / k
    
    # Normalize the effective chances to sum up to 100%
    total_effective_chance = sum(effective_chances)
    final_effective_chances = [chance / total_effective_chance * 100 for chance in effective_chances]
    
    return final_effective_chances

# Read input
n, k = map(int, input().split())
spawn_chances = list(map(float, input().split()))

# Compute and output the effective spawn chances
effective_chances = effective_spawn_chances(n, k, spawn_chances)
print(" ".join("{:.6f}".format(chance) for chance in effective_chances))