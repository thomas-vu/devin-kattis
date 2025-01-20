def solve_gear_ratios(gear_ratios):
    from fractions import Fraction
    
    # Read the gear ratios
    front_ratios = []
    rear_ratios = []
    
    for ratio in gear_ratios:
        n, d = map(int, ratio.split('/'))
        front_ratios.append((n, d))
    
    # Generate all possible combinations of front and rear sprocket sizes
    for i in range(1, 7):
        for j in range(i+1, 7):
            rear_sprockets = [i, j]
            for k in range(1, 13):
                for l in range(k+1, 13):
                    front_sprockets = [k, l]
                    # Check if this combination of sprocket sizes can produce the given gear ratios
                    valid = True
                    for front_ratio, rear_ratio in zip(front_ratios, rear_ratios):
                        if Fraction(front_ratio[0], front_ratio[1]) / Fraction(rear_sprockets[0], rear_sprockets[1]) != Fraction(*rear_ratio):
                            valid = False
                            break
                    if valid:
                        return front_sprockets, rear_sprockets
    
    # If no valid combination is found, return "impossible"
    return "impossible"

# Read the input data
gear_ratios = []
for _ in range(12):
    gear_ratios.append(input().strip())

# Solve the problem and output the result
result = solve_gear_ratios(gear_ratios)
if result == "impossible":
    print("impossible")
else:
    front_sprockets, rear_sprockets = result
    print(*front_sprockets)
    print(*rear_sprockets)