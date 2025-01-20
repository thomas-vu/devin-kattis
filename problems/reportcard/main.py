MOD = 10**9 + 7

def count_gpa(N, report_card):
    # Convert the grades to points
    grade_points = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
    points = [grade_points[c] for c in report_card]
    
    def calculate_gpa(points):
        return sum(points) / len(points)
    
    def count_variations(start, points):
        if start == N:
            current_gpa = calculate_gpa(points)
            old_gpa = (sum([4, 3, 3]) / 3)
            return int(current_gpa > old_gpa)
        
        count = 0
        for grade in ['A', 'B', 'C', 'D', 'F']:
            new_points = points + [grade_points[grade]]
            count += count_variations(start + 1, new_points)
        return count % MOD
    
    return count_variations(0, [])

# Read input
N = int(input())
report_card = input()

# Calculate and print the result
result = count_gpa(N, report_card)
print(result)