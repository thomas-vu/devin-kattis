def is_valid(s):
    stack = []
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        elif stack and stack[-1] == '(':
            stack.pop()
        else:
            return False
    return not stack

def can_make_valid(n, matrix):
    for i in range(n):
        if not is_valid(matrix[i]):
            for j in range(n):
                for k in range(j + 1, n):
                    new_matrix = [row[:] for row in matrix]
                    new_matrix[i][j], new_matrix[i][k] = new_matrix[i][k], new_matrix[i][j]
                    if is_valid(new_matrix[i]):
                        break
                else:
                    continue
                break
            else:
                return "No"
    return "Yes"

n = int(input())
matrix = [list(input().strip()) for _ in range(n)]
print(can_make_valid(n, matrix))