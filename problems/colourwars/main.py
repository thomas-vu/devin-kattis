def minimum_students(N, responses):
    students = [0] * (max(responses) + 1)
    for response in responses:
        students[response] += 1
    
    min_students = N + sum(students[:-1])
    return min_students

# Read input
N = int(input())
responses = list(map(int, input().split()))

# Output the result
print(minimum_students(N, responses))