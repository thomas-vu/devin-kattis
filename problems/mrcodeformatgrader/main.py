C, N = map(int, input().split())
errors = list(map(int, input().split()))

# Helper function to compress line numbers with errors and correct lines
def compress_line_numbers(start, end):
    if start == end:
        return str(start)
    else:
        return f"{start}-{end}"

# Compress errors and correct lines
errors_list = []
correct_lines = []
i = 1
while i <= C:
    if i in errors:
        j = i
        while j < C and j + 1 in errors:
            j += 1
        if j > i:
            errors_list.append(compress_line_numbers(i, j))
            i = j + 1
        else:
            errors_list.append(str(i))
            i += 1
    else:
        correct_lines.append(str(i))
        i += 1

# Output the results
print("Errors:", ", ".join(errors_list))
print("Correct:", ", ".join(correct_lines))