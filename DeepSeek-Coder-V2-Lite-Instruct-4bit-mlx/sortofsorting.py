def sort_student_names(test_cases):
    for case in test_cases:
        n = int(case[0])
        names = [line.strip() for line in case[1:]]
        # Sort using the first two letters of each name
        names.sort(key=lambda x: x[:2].lower())
        for name in names:
            print(name)
        print()  # Print a blank line after each test case

# Read input from stdin
import sys
input_lines = sys.stdin.readlines()
i = 0
test_cases = []
while i < len(input_lines):
    n = int(input_lines[i].strip())
    if n == 0:
        break
    case = [input_lines[j].strip() for j in range(i + 1, i + n + 1)]
    test_cases.append(case)
    i += n + 1

# Process and output the sorted names
sort_student_names(test_cases)