def count_unclaimed_trees(n, m, people, trees):
    tree_claims = {}
    
    for person in people:
        min_distance = float('inf')
        closest_tree = -1
        
        for tree in trees:
            distance = abs(person - tree)
            if distance < min_distance:
                min_distance = distance
                closest_tree = tree
            elif distance == min_distance:
                continue
        
        if closest_tree not in tree_claims:
            tree_claims[closest_tree] = 1
        else:
            tree_claims[closest_tree] += 1
    
    unclaimed_count = m - len(tree_claims)
    return unclaimed_count

# Read input
n, m = map(int, input().split())
people = list(map(int, input().split()))
trees = list(map(int, input().split()))

# Calculate and output the number of unclaimed trees
print(count_unclaimed_trees(n, m, people, trees))