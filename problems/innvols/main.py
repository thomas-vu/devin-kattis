from collections import defaultdict
import sys

# Read the input from stdin
data = input().strip()

# Initialize a dictionary to store sections and their counts
sections_count = defaultdict(int)

# Iterate over all possible sections in the data
for start in range(len(data)):
    for end in range(start, len(data)):
        section = data[start:end+1]
        sections_count[section] += 1

# Convert the dictionary to a list of tuples and sort it
sections_list = [(count, section) for section, count in sections_count.items()]
sections_list.sort(key=lambda x: (-x[0], x[1]))

# Print the results
for count, section in sections_list:
    print(count, section)