def calculate_workout_time(jim, people):
    jim_schedule = []
    for i in range(3):
        for j in range(10):
            start_time = max(jim[j] + i * (jim[10+j] + jim[20+j]), people[j][2])
            end_time = start_time + jim[j]
            jim_schedule.append((start_time, end_time))
    
    for i in range(10):
        for j in range(i, 10):
            for k in range(3):
                for l in range(10):
                    if j != l:
                        start_time = max(jim_schedule[i*3+k][1], people[l][2])
                        end_time = start_time + jim[j]
                        jim_schedule.append((start_time, end_time))
    
    return jim_schedule[-1][1]

# Read input
jim = list(map(int, input().split()))
people = [list(map(int, input().split())) for _ in range(10)]

# Calculate and output the result
print(calculate_workout_time(jim, people))