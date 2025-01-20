def find_department_chair(n, opus_numbers):
    # Initialize the list of faculty members with their corresponding opus numbers
    faculty = [(i + 1, opus_numbers[i]) for i in range(n)]
    
    index = 0
    while len(faculty) > 1:
        # Determine the next index to remove based on the count-off process
        index = (index + faculty[index][1] - 1) % len(faculty)
        # Remove the faculty member at the determined index
        faculty.pop(index)
    
    # Return the number of the new department chair (the last remaining faculty member)
    return faculty[0][0]

# Read input from stdin
n = int(input().strip())
opus_numbers = list(map(int, input().strip().split()))

# Output the result
print(find_department_chair(n, opus_numbers))