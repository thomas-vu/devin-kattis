def count_problems(input_str):
    problems = input_str.split(';')
    count = 0
    for problem in problems:
        if '-' in problem:
            start, end = map(int, problem.split('-'))
            count += (end - start + 1)
        else:
            count += 1
    return count

# Read input from stdin
input_str = input().strip()

# Output the result
print(count_problems(input_str))