def determine_magma_type(n, operations):
    # Check for associativity (P1)
    associative = True
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if operations[i][operations[j][k]] != operations[operations[i][j]][k]:
                    associative = False
                    break
            if not associative:
                break
        if not associative:
            break
    
    # Check for identity element (P2)
    identity_element = None
    for x in range(n):
        found = False
        for i in range(n):
            for j in range(n):
                if operations[i][j] == x and i != j:
                    found = True
                    break
            if found:
                break
        if not found:
            identity_element = x
    
    # Check for inverses (P3)
    has_inverses = True
    if identity_element is None:
        has_inverses = False
    else:
        for x in range(n):
            found_inverse = False
            for y in range(n):
                if operations[x][y] == identity_element and operations[y][x] == identity_element:
                    found_inverse = True
                    break
            if not found_inverse:
                has_inverses = False
                break
    
    if associative and has_inverses:
        return "group"
    elif associative and identity_element is not None:
        return "monoid"
    elif associative:
        return "semigroup"
    else:
        return "magma"

# Read input
n = int(input())
operations = [[0] * n for _ in range(n)]
for _ in range(n * n):
    i, j, k = map(int, input().split())
    operations[i][j] = k

# Determine the type of magma
result = determine_magma_type(n, operations)
print(result)