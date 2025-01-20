def find_operations(abilities):
    # Check if it's possible to exploit all weaknesses
    if not is_possible(abilities):
        return "IMPOSSIBLE"
    
    # Find the minimum number of operations needed
    min_operations = float('inf')
    for mask in range(1, 1 << 7):
        if is_valid_plan(abilities, mask):
            min_operations = min(min_operations, bin(mask).count('1'))
    
    # If no valid plan found, return IMPOSSIBLE
    if min_operations == float('inf'):
        return "IMPOSSIBLE"
    
    # Find the actual operations for the minimum number of operations
    best_plan = (1 << 7) - 1
    for mask in range(1, 1 << 7):
        if bin(mask).count('1') == min_operations and is_valid_plan(abilities, mask):
            best_plan = mask
            break
    
    # Output the operations
    operations = []
    while best_plan:
        operation = []
        members = 0
        for i in range(7):
            if best_plan & (1 << i):
                operation.append((i + 1, [j for j in range(7) if abilities[i][j] == 1]))
                members += 1
        operations.append((members, operation))
        best_plan &= ~(best_plan & -best_plan)
    
    print(min_operations)
    for operation in operations:
        print(operation[0])
        for member, weaknesses in operation[1]:
            print(f"{['Twilight Sparkle', 'Applejack', 'Rarity', 'Pinkie Pie', 'Fluttershy', 'Rainbow Dash', 'Spike'][member - 1]} {weaknesses[0] + 1}")

def is_possible(abilities):
    # Check if it's possible to exploit all weaknesses
    for i in range(7):
        count = 0
        for j in range(7):
            if abilities[i][j] == 1:
                count += 1
        if count == 0:
            return False
    return True

def is_valid_plan(abilities, mask):
    # Check if the plan with the given mask is valid
    exploited_weaknesses = [0] * 7
    for i in range(7):
        if mask & (1 << i):
            for j in range(7):
                if abilities[i][j] == 1:
                    exploited_weaknesses[j] += 1
    for count in exploited_weaknesses:
        if count != 1:
            return False
    return True

# Read input
abilities = [list(map(int, input().split())) for _ in range(7)]
find_operations(abilities)