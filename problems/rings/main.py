def is_overlapping(ring1, ring2):
    x1, y1, r1 = ring1
    x2, y2, r2 = ring2
    distance_centers = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distance_centers <= (r1 + r2)

def find_largest_component(rings):
    n = len(rings)
    parent = list(range(n))
    
    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]
    
    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_j] = root_i
    
    for i in range(n):
        for j in range(i + 1, n):
            if is_overlapping(rings[i], rings[j]):
                union(i, j)
    
    component_count = {}
    for i in range(n):
        root = find(i)
        if root not in component_count:
            component_count[root] = 0
        component_count[root] += 1
    
    largest_component = max(component_count.values(), default=0)
    return largest_component

def main():
    while True:
        n = int(input())
        if n == -1:
            break
        rings = []
        for _ in range(n):
            x, y, r = map(float, input().split())
            rings.append((x, y, r))
        largest_component = find_largest_component(rings)
        if largest_component == 1:
            print("The largest component contains 1 ring.")
        else:
            print(f"The largest component contains {largest_component} rings.")

if __name__ == "__main__":
    main()