def max_pyramid_height(N):
    height = 0
    blocks = N
    while blocks > height * (height + 1) / 2:
        height += 1
        blocks -= height * (height + 1) / 2
    return height - int(blocks != 0)

# Read input from stdin
N = int(input().strip())
print(max_pyramid_height(N))