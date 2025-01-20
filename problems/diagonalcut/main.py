m, n = map(int, input().split())

# Calculate the number of blocks cut into two equal pieces
blocks_cut = (m * n) // 2
print(blocks_cut)