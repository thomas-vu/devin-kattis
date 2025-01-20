def total_bags_of_popcorn(n):
    # Number of groups each with n/4 participants
    num_groups = 4
    # Each group has (n/4) * (n/4 - 1) / 2 matches
    group_matches = (n // 4) * ((n // 4) - 1) // 2
    # Total matches in all groups
    total_matches = num_groups * group_matches
    
    # Semi-finals and finals are 2 extra bags each
    semi_finals = 2
    final = 1
    
    # Total bags needed is the sum of group matches, semi-finals, and final
    total_bags = total_matches + semi_finals + final
    
    return total_bags

# Example usage:
n = int(input())
print(total_bags_of_popcorn(n))