def min_students_heard(r, c, d, students):
    # Create a set of all possible positions in the library
    all_positions = {(i, j) for i in range(1, r + 1) for j in range(1, c + 1)}
    
    # Remove the positions of students who are already studying
    for student in students:
        all_positions.remove(student)
    
    min_heard = float('inf')
    
    # Check each empty table to see how many students can be heard
    for pos in all_positions:
        count = 0
        for student in students:
            if (pos[0] - student[0]) ** 2 + (pos[1] - student[1]) ** 2 <= d**2:
                count += 1
        min_heard = min(min_heard, count)
    
    return min_heard if min_heard != float('inf') else 0

# Read input
r, c, d, n = map(int, input().split())
students = [tuple(map(int, input().split())) for _ in range(n)]

# Get the result and print it
result = min_students_heard(r, c, d, students)
print(result)