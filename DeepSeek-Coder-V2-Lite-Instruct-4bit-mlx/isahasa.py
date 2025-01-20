def main():
    n, m = map(int, input().split())
    
    # Read is-a and has-a relationships
    relations = {}
    for _ in range(n):
        c1, r, c2 = input().split()
        if c1 not in relations:
            relations[c1] = {'is-a': set(), 'has-a': set()}
        if r == 'is-a':
            relations[c1]['is-a'].add(c2)
        else:
            relations[c1]['has-a'].add(c2)
    
    # Process queries
    for query_num in range(1, m + 1):
        c1, q, c2 = input().split()
        if q == 'is-a':
            result = check_isa(c1, c2, relations)
        else:
            result = check_hasa(c1, c2, relations)
        print(f"Query {query_num}: {'true' if result else 'false'}")

def check_isa(c1, c2, relations):
    if c1 == c2:
        return True
    stack = [c1]
    visited = set()
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        for subclass in relations[current]['is-a']:
            if subclass == c2:
                return True
            stack.append(subclass)
    return False

def check_hasa(c1, c2, relations):
    if c1 == c2:
        return True
    stack = [c1]
    visited = set()
    while stack:
        current = stack.pop()
        if current in visited:
            continue
        visited.add(current)
        for field in relations[current]['has-a']:
            if field == c2:
                return True
            stack.append(field)
    return False

if __name__ == "__main__":
    main()