from collections import defaultdict

# Read the number of contestants
N = int(input())

# Initialize a dictionary to store locations and counts
locations_count = defaultdict(int)

# Read the contestants' information
for _ in range(N):
    first_name = input().strip()
    location = input().strip()
    locations_count[location] += 1

# Output the results
for location, count in locations_count.items():
    print(location, count)