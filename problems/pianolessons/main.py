def max_students(N, M, students):
    # Create a list to store the number of time slots available for each student
    availability = [0] * M
    
    # Mark the time slots that are available for each student
    for student in students:
        for slot in student[1:]:
            availability[slot - 1] += 1
    
    # Sort the students based on the number of available time slots in descending order
    sorted_students = sorted(students, key=lambda x: sum(x[1:]), reverse=True)
    
    # Try to assign the students with more available slots first
    assigned_slots = [False] * M
    count = 0
    
    for student in sorted_students:
        assigned = False
        for slot in student[1:]:
            if not assigned_slots[slot - 1] and availability[slot - 1] > 0:
                assigned_slots[slot - 1] = True
                availability[slot - 1] -= 1
                count += 1
                assigned = True
                break
        if not assigned:
            for slot in student[1:]:
                if availability[slot - 1] > 0:
                    availability[slot - 1] -= 1
                    count += 1
                    break
    
    return count

# Read input
N, M = map(int, input().split())
students = [list(map(int, input().split())) for _ in range(N)]

# Get the maximum number of students Mrs. Mackenzie can fit into her schedule
result = max_students(N, M, students)
print(result)