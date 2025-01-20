def max_activities(n, k, activities):
    # Sort activities by their ending time
    activities.sort(key=lambda x: (x[1], x[0]))
    
    classrooms = [0] * k
    count = 0
    
    for s, f in activities:
        assigned = False
        for j in range(k):
            if classrooms[j] <= s:
                classrooms[j] = f
                count += 1
                assigned = True
                break
        if not assigned:
            classrooms[count] = f  # Assign to the next available classroom
    
    return count

# Read input
n, k = map(int, input().split())
activities = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_activities(n, k, activities))