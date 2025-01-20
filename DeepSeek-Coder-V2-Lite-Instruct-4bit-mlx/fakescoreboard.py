def solve(T, P, solved_by_teams, problems_solved):
    from itertools import permutations
    
    # Check if the sum of solved_by_teams matches the sum of problems_solved
    if sum(solved_by_teams) != sum(problems_solved):
        return "Impossible"
    
    # Generate all possible solutions and check if any match the solved_by_teams and problems_solved
    for perm in permutations(range(P)):
        solution = [['N' for _ in range(P)] for _ in range(T)]
        valid = True
        
        # Assign Y or N based on the permutation
        for i in range(T):
            for j in range(P):
                if solved_by_teams[i] == problems_solved[perm[j]]:
                    solution[i][perm[j]] = 'Y'
        
        # Check if the current solution matches solved_by_teams and problems_solved
        actual_solved = [0] * P
        for i in range(T):
            for j in range(P):
                if solution[i][j] == 'Y':
                    actual_solved[j] += 1
        
        if actual_solved == problems_solved:
            return '\n'.join(''.join(row) for row in solution)
    
    return "Impossible"

while True:
    line = input().strip()
    if line == "0 0":
        break
    
    T, P = map(int, line.split())
    solved_by_teams = list(map(int, input().strip().split()))
    problems_solved = list(map(int, input().strip().split()))
    
    result = solve(T, P, solved_by_teams, problems_solved)
    print(result)
    print()