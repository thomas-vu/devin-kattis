import sys
from collections import defaultdict

# Read input from stdin
n = int(sys.stdin.readline().strip())
trips = []
country_dict = defaultdict(list)
for _ in range(n):
    country, year = sys.stdin.readline().strip().split()
    year = int(year)
    trips.append((country, year))
    country_dict[country].append(year)

q = int(sys.stdin.readline().strip())
queries = []
for _ in range(q):
    country, k = sys.stdin.readline().strip().split()
    k = int(k)
    queries.append((country, k))

# Sort the years for each country and create a map to quickly find the k-th trip year
for country in country_dict:
    country_dict[country].sort()

# Process queries and output results
for country, k in queries:
    years = country_dict[country]
    print(years[k - 1])