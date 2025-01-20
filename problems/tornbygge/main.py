def build_towers(N, bricks):
    towers = []
    for brick in bricks:
        if not towers or brick > towers[-1]:
            towers.append(brick)
        else:
            low = 0
            high = len(towers) - 1
            while low <= high:
                mid = (low + high) // 2
                if towers[mid] < brick:
                    low = mid + 1
                else:
                    high = mid - 1
            towers[low] = brick
    return len(towers)

# Read input
N = int(input())
bricks = list(map(int, input().split()))

# Output the number of towers built
print(build_towers(N, bricks))