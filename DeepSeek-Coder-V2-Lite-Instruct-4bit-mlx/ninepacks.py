def min_packs(hotdog_packs, bun_packs):
    hotdogs = sum(hotdog_packs)
    buns = sum(bun_packs)
    
    if hotdogs % buns != 0:
        return "impossible"
    
    target = hotdogs // buns
    
    min_packs = float('inf')
    
    for i in range(len(hotdog_packs)):
        for j in range(len(bun_packs)):
            if hotdog_packs[i] % bun_packs[j] == 0:
                temp = hotdog_packs[i] // bun_packs[j]
                for k in range(temp, temp * target + 1, temp):
                    if hotdogs == k * buns:
                        min_packs = min(min_packs, i + j + (hotdog_packs[i] // k))
    
    return min_packs if min_packs != float('inf') else "impossible"

# Read input
H = int(input())
hotdog_packs = list(map(int, input().split()))
B = int(input())
bun_packs = list(map(int, input().split()))

# Output the result
print(min_packs(hotdog_packs, bun_packs))