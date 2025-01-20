def best_lowest_score(n, k, answers):
    # Convert each student's answers to a list of points (1 for T, 0 for F)
    points = [[1 if c == 'T' else 0 for c in answer] for answer in answers]
    
    # Calculate the total points for each student and sum them up
    total_points = [sum(student) for student in points]
    
    # Sort the total points to find the best possible lowest score
    total_points.sort()
    
    # The best possible lowest score is the minimum of the total points
    return total_points[0]

# Read input
n, k = map(int, input().split())
answers = [input() for _ in range(n)]

# Output the best possible lowest score
print(best_lowest_score(n, k, answers))