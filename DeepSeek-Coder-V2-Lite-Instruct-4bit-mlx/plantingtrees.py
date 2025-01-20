import sys

def earliest_party_day(tree_days):
    max_growth_time = max(tree_days)
    return max_growth_time + 1

# Read input from stdin
n = int(input().strip())
tree_days = list(map(int, input().strip().split()))

# Calculate and output the earliest party day
print(earliest_party_day(tree_days))