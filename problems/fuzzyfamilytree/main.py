def find_possible_enars(n, relations):
    parent_map = {}
    
    for relation in relations:
        a, b = map(int, relation.split())
        if '?' in relation:
            parent_map[a] = b
    
    possible_enars = set(range(n))
    
    for relation in relations:
        a, b = map(int, relation.split())
        if '>' in relation:
            parent_map[b] = a
    
    for child, parent in parent_map.items():
        possible_enars.discard(child)
    
    return sorted(possible_enars)

# Read input
n = int(input())
relations = [input() for _ in range(n - 1)]

# Output the result
possible_enars = find_possible_enars(n, relations)
print(' '.join(map(str, possible_enars)))