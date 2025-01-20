import math

def min_jumps(pages):
    max_page = 0
    jumps = 0
    current_position = 0
    
    for page in pages:
        while max_page < page:
            max_page += 2 ** (math.floor(math.log2(max_page + 1)))
            jumps += 1
        max_page = max(max_page, page)
    
    return jumps

# Read input
N = int(input())
pages = [int(input()) for _ in range(N)]

# Calculate and output the result
print(min_jumps(pages))