def max_damage(n, m, k):
    # The optimal strategy is to create groups of size (n // m) + 1 and the rest smaller groups
    large_groups = n // (k + 1)
    small_groups = m - large_groups
    
    # Calculate the damage caused by large groups in one turn
    initial_damage = large_groups * (k + 1)
    
    # Calculate the remaining gnomes after one turn of large groups
    remaining_gnomes = n - initial_damage
    
    # Calculate the damage for each subsequent turn until all gnomes are killed
    damage = initial_damage
    turns = 1
    while remaining_gnomes > 0:
        # The number of gnomes killed in each turn after the initial one
        if remaining_gnomes <= k:
            damage += remaining_gnomes
            break
        else:
            damage += k
            remaining_gnomes -= k
        turns += 1
    
    return damage

# Read input from stdin
n, m, k = map(int, input().split())
print(max_damage(n, m, k))