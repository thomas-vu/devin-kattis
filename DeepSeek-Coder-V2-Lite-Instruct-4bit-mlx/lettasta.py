def find_easiest_problem(N, problem_names, scores):
    total_scores = [0] * N
    for team in scores:
        for i, score in enumerate(team):
            total_scores[i] += score
    max_score = max(total_scores)
    for i, total in enumerate(total_scores):
        if total == max_score:
            return problem_names[i]

# Read input
N = int(input())
M = int(input())
problem_names = input().split()
scores = [list(map(int, input().split())) for _ in range(M)]

# Find and print the easiest problem
easiest_problem = find_easiest_problem(N, problem_names, scores)
print(easiest_problem)