def min_max_distance(students, tutors):
    max_distances = []
    
    for student in students:
        min_distance = float('inf')
        for tutor in tutors:
            distance = abs(student[0] - tutor[0]) + abs(student[1] - tutor[1])
            if distance < min_distance:
                min_distance = distance
        max_distances.append(min_distance)
    
    return min(max_distances)

N = int(input())
students = [tuple(map(int, input().split())) for _ in range(N)]
tutors = [tuple(map(int, input().split())) for _ in range(N)]

K = min_max_distance(students, tutors)
print(K)