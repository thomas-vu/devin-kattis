def max_skill_level(n, s, problems):
    # Sort the problems based on the lower bound
    problems.sort(key=lambda x: x[0])
    
    current_skill = s
    
    for l, r in problems:
        if l <= current_skill <= r:
            # Solve the problem and increase skill level by 1
            current_skill += 1
        # If the problem cannot be solved, skip it as per the rules
    
    return current_skill

# Read input
n, s = map(int, input().split())
problems = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_skill_level(n, s, problems))