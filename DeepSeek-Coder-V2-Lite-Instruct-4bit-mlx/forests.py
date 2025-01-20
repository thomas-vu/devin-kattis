def count_opinions(P, T, pairs):
    heard_trees = {}
    for person, tree in pairs:
        if person not in heard_trees:
            heard_trees[person] = set()
        heard_trees[person].add(tree)
    
    unique_opinions = set()
    for opinion in heard_trees.values():
        unique_opinions.add(frozenset(opinion))
    
    return len(unique_opinions)

# Read input
import sys
input_data = sys.stdin.readlines()
P, T = map(int, input_data[0].split())
pairs = [tuple(map(int, line.split())) for line in input_data[1:]]

# Output the result
print(count_opinions(P, T, pairs))