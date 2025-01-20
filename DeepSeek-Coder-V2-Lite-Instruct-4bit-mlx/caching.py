def min_reads(c, n, accesses):
    cache = set()
    reads = 0
    
    for obj in accesses:
        if obj not in cache:
            if len(cache) < c:
                cache.add(obj)
            else:
                # Evict the least recently used object (LRU)
                cache.remove(min(cache, key=lambda x: accesses.index([a for a in accesses if a == x]))
            reads += 1
    return reads

# Read input
c, n, a = map(int, input().split())
accesses = [int(input()) for _ in range(a)]

# Output the result
print(min_reads(c, n, accesses))