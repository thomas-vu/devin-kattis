from collections import defaultdict
import sys

# Read input from stdin
trees = []
for line in sys.stdin:
    trees.append(line.strip())

# Count the occurrences of each tree species
species_count = defaultdict(int)
for tree in trees:
    species_count[tree] += 1

# Calculate the total number of trees
total_trees = len(trees)

# Calculate the percentage of each species
species_percentages = {}
for species, count in species_count.items():
    percentage = (count / total_trees) * 100
    species_percentages[species] = percentage

# Print the results in alphabetical order by ASCII value
for species in sorted(species_percentages.keys()):
    print(f"{species} {species_percentages[species]:.8f}")